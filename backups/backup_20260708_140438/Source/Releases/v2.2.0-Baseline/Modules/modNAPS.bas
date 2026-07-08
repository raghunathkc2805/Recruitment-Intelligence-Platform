Attribute VB_Name = "modNAPS"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' NAPS Engine
' Version 2.0.1
'==========================================================

Public Sub ProcessNAPSMail(ByVal Mail As Outlook.MailItem)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim CandidateID As String
    Dim NAPSID As String
    Dim NextRow As Long

    CandidateName = ParseCandidateName(Mail)

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    NAPSID = GenerateNextNAPSID()

    NextRow = GetNextRow(wsNAPS)

    With wsNAPS

        .Cells(NextRow, 1).Value = NAPSID
        .Cells(NextRow, 2).Value = CandidateID
        .Cells(NextRow, 3).Value = CandidateName
        .Cells(NextRow, 4).Value = Date
        .Cells(NextRow, 5).Value = ""
        .Cells(NextRow, 6).Value = "Pending"
        .Cells(NextRow, 7).Value = Mail.Subject
        .Cells(NextRow, 8).Value = Mail.EntryID
        .Cells(NextRow, 9).Value = Now
        .Cells(NextRow, 10).Value = Now

    End With

    AddTimeline _
        CandidateID, _
        CandidateName, _
        "NAPS Registration", _
        NAPSID

    Exit Sub

ErrorHandler:

    LogError "modNAPS", _
             "ProcessNAPSMail", _
             Err.Number, _
             Err.Description

End Sub

Public Function GenerateNextNAPSID() As String

    Static NAPSNo As Long

    NAPSNo = NAPSNo + 1

    GenerateNextNAPSID = _
        "NAP" & Format(NAPSNo, "000000")

End Function

