Attribute VB_Name = "modDeviation"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Deviation Engine
' Version 2.0.1
'==========================================================

Public Sub ProcessDeviationMail(ByVal Mail As Outlook.MailItem)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim CandidateID As String
    Dim DeviationID As String
    Dim NextRow As Long

    CandidateName = ParseCandidateName(Mail)

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    DeviationID = GenerateNextDeviationID()

    NextRow = GetNextRow(wsDeviation)

    With wsDeviation

        .Cells(NextRow, 1).Value = DeviationID
        .Cells(NextRow, 2).Value = CandidateID
        .Cells(NextRow, 3).Value = CandidateName
        .Cells(NextRow, 4).Value = "General"
        .Cells(NextRow, 5).Value = Mail.SenderName
        .Cells(NextRow, 6).Value = ""
        .Cells(NextRow, 7).Value = Date
        .Cells(NextRow, 8).Value = ""
        .Cells(NextRow, 9).Value = "Pending"
        .Cells(NextRow, 10).Value = Mail.EntryID
        .Cells(NextRow, 11).Value = ""
        .Cells(NextRow, 12).Value = Now
        .Cells(NextRow, 13).Value = Now

    End With

    AddTimeline _
        CandidateID, _
        CandidateName, _
        "Deviation Raised", _
        DeviationID

    Exit Sub

ErrorHandler:

    LogError "modDeviation", _
             "ProcessDeviationMail", _
             Err.Number, _
             Err.Description

End Sub

Public Function GenerateNextDeviationID() As String

    Static DevNo As Long

    DevNo = DevNo + 1

    GenerateNextDeviationID = _
        "DEV" & Format(DevNo, "000000")

End Function

