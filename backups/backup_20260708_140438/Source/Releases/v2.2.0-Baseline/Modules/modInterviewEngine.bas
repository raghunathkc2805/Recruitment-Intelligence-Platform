Attribute VB_Name = "modInterviewEngine"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Interview Engine
' Version 2.0.1
'==========================================================

Public Sub ProcessInterviewMail(ByVal Mail As Outlook.MailItem)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim CandidateID As String
    Dim InterviewID As String
    Dim NextRow As Long

    CandidateName = ParseCandidateName(Mail)

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    InterviewID = GenerateNextInterviewID()

    NextRow = GetNextRow(wsInterviews)

    With wsInterviews

        .Cells(NextRow, 1).Value = InterviewID
        .Cells(NextRow, 2).Value = CandidateID
        .Cells(NextRow, 3).Value = CandidateName
        .Cells(NextRow, 4).Value = ""
        .Cells(NextRow, 5).Value = ""
        .Cells(NextRow, 6).Value = Mail.SenderName
        .Cells(NextRow, 7).Value = Date
        .Cells(NextRow, 8).Value = Time
        .Cells(NextRow, 9).Value = "Email"
        .Cells(NextRow, 10).Value = "Scheduled"
        .Cells(NextRow, 11).Value = ""
        .Cells(NextRow, 12).Value = ""
        .Cells(NextRow, 13).Value = Mail.EntryID
        .Cells(NextRow, 14).Value = ""
        .Cells(NextRow, 15).Value = Now
        .Cells(NextRow, 16).Value = Now

    End With

    AddTimeline _
        CandidateID, _
        CandidateName, _
        "Interview Scheduled", _
        InterviewID

    Exit Sub

ErrorHandler:

    LogError "modInterviewEngine", _
             "ProcessInterviewMail", _
             Err.Number, _
             Err.Description

End Sub

Public Function GenerateNextInterviewID() As String

    Static InterviewNo As Long

    InterviewNo = InterviewNo + 1

    GenerateNextInterviewID = _
        "INT" & Format(InterviewNo, "000000")

End Function

