Attribute VB_Name = "modBGV"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' BGV Engine
' Version 2.0.1
'==========================================================

Public Sub ProcessBGVMail(ByVal Mail As Outlook.MailItem)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim CandidateID As String
    Dim BGVID As String
    Dim NextRow As Long

    CandidateName = ParseCandidateName(Mail)

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    BGVID = GenerateNextBGVID()

    NextRow = GetNextRow(wsBGV)

    With wsBGV

        .Cells(NextRow, 1).Value = BGVID
        .Cells(NextRow, 2).Value = CandidateID
        .Cells(NextRow, 3).Value = CandidateName
        .Cells(NextRow, 4).Value = ""
        .Cells(NextRow, 5).Value = Date
        .Cells(NextRow, 6).Value = ""
        .Cells(NextRow, 7).Value = "Standard"
        .Cells(NextRow, 8).Value = "Initiated"
        .Cells(NextRow, 9).Value = ""
        .Cells(NextRow, 10).Value = ""
        .Cells(NextRow, 11).Value = Now
        .Cells(NextRow, 12).Value = Now

    End With

    AddTimeline _
        CandidateID, _
        CandidateName, _
        "BGV Initiated", _
        BGVID

    Exit Sub

ErrorHandler:

    LogError "modBGV", _
             "ProcessBGVMail", _
             Err.Number, _
             Err.Description

End Sub

Public Function GenerateNextBGVID() As String

    Static BGVNo As Long

    BGVNo = BGVNo + 1

    GenerateNextBGVID = _
        "BGV" & Format(BGVNo, "000000")

End Function

