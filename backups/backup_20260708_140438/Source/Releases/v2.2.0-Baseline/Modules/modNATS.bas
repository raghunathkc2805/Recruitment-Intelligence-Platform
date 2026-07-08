Attribute VB_Name = "modNATS"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' NATS Engine
' Version 2.0.1
'==========================================================

Public Sub ProcessNATSMail(ByVal Mail As Outlook.MailItem)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim CandidateID As String
    Dim NATSID As String
    Dim NextRow As Long

    CandidateName = ParseCandidateName(Mail)

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    NATSID = GenerateNextNATSID()

    NextRow = GetNextRow(wsNATS)

    With wsNATS

        .Cells(NextRow, 1).Value = NATSID
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
        "NATS Registration", _
        NATSID

    Exit Sub

ErrorHandler:

    LogError "modNATS", _
             "ProcessNATSMail", _
             Err.Number, _
             Err.Description

End Sub

Public Function GenerateNextNATSID() As String

    Static NATSNo As Long

    NATSNo = NATSNo + 1

    GenerateNextNATSID = _
        "NAT" & Format(NATSNo, "000000")

End Function

