Attribute VB_Name = "modResources"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modResources
'==========================================================

Public Sub ProcessResourceMail(ByVal Mail As Outlook.MailItem, _
                               ByVal FolderPath As String)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim Parts() As String
    Dim NextRow As Long
    Dim CandidateID As String

    Parts = Split(Mail.Subject, "-")

    If UBound(Parts) < 0 Then Exit Sub

    CandidateName = CleanText(Parts(0))

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    SaveAttachments Mail, CandidateName

    ProcessResume Mail, CandidateName

    NextRow = GetNextRow(wsResources)

    wsResources.Cells(NextRow, 1).Value = CandidateID
    wsResources.Cells(NextRow, 2).Value = Mail.ReceivedTime
    wsResources.Cells(NextRow, 3).Value = CandidateName

    If UBound(Parts) >= 1 Then wsResources.Cells(NextRow, 4).Value = CleanText(Parts(1))
    If UBound(Parts) >= 2 Then wsResources.Cells(NextRow, 6).Value = CleanText(Parts(2))
    If UBound(Parts) >= 3 Then wsResources.Cells(NextRow, 7).Value = CleanText(Parts(3))

    wsResources.Cells(NextRow, 22).Value = Mail.Subject
    wsResources.Cells(NextRow, 23).Value = Mail.SenderName
    wsResources.Cells(NextRow, 24).Value = Mail.SenderEmailAddress
    wsResources.Cells(NextRow, 25).Value = Mail.EntryID
    wsResources.Cells(NextRow, 26).Value = "Processed"
    wsResources.Cells(NextRow, 28).Value = Now
    wsResources.Cells(NextRow, 29).Value = Now

    Exit Sub

ErrorHandler:

    LogError "modResources", _
             "ProcessResourceMail", _
             Err.Number, _
             Err.Description

End Sub

