Attribute VB_Name = "modResume"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modResume
'==========================================================

Public Sub ProcessResume(ByVal Mail As Outlook.MailItem, _
                         ByVal CandidateName As String)

    On Error GoTo ErrorHandler

    SaveAttachments Mail, CandidateName

    IndexResume Mail, CandidateName

    UpdateCandidateMaster Mail, CandidateName

    Exit Sub

ErrorHandler:

    LogError "modResume", _
             "ProcessResume", _
             Err.Number, _
             Err.Description

End Sub

Private Sub IndexResume(ByVal Mail As Outlook.MailItem, _
                        ByVal CandidateName As String)

    Dim Atmt As Outlook.Attachment
    Dim NextRow As Long
    Dim SavePath As String

    For Each Atmt In Mail.Attachments

        If IsResumeFile(Atmt.FileName) Then

            SavePath = GetSetting("CANDIDATE_FOLDER") & "\" & _
                       CleanFolderName(CandidateName) & _
                       "\Resumes\" & Atmt.FileName

            NextRow = GetNextRow(wsResume)

            wsResume.Cells(NextRow, 1).Value = CandidateName
            wsResume.Cells(NextRow, 2).Value = Atmt.FileName
            wsResume.Cells(NextRow, 3).Value = SavePath
            wsResume.Cells(NextRow, 4).Value = Mail.Subject
            wsResume.Cells(NextRow, 5).Value = Mail.SenderName
            wsResume.Cells(NextRow, 6).Value = Mail.ReceivedTime
            wsResume.Cells(NextRow, 7).Value = ""
            wsResume.Cells(NextRow, 8).Value = ""
            wsResume.Cells(NextRow, 9).Value = ""
            wsResume.Cells(NextRow, 10).Value = Mail.EntryID

        End If

    Next

End Sub

Private Sub UpdateCandidateMaster(ByVal Mail As Outlook.MailItem, _
                                  ByVal CandidateName As String)

    Dim NextRow As Long

    NextRow = GetNextRow(wsCandidatesMaster)

    wsCandidatesMaster.Cells(NextRow, 1).Value = GenerateCandidateID()
    wsCandidatesMaster.Cells(NextRow, 2).Value = CandidateName
    wsCandidatesMaster.Cells(NextRow, 3).Value = Mail.SenderEmailAddress
    wsCandidatesMaster.Cells(NextRow, 4).Value = ""
    wsCandidatesMaster.Cells(NextRow, 5).Value = ""
    wsCandidatesMaster.Cells(NextRow, 6).Value = ""
    wsCandidatesMaster.Cells(NextRow, 7).Value = _
        GetSetting("CANDIDATE_FOLDER") & "\" & CleanFolderName(CandidateName)
    wsCandidatesMaster.Cells(NextRow, 8).Value = "Active"
    wsCandidatesMaster.Cells(NextRow, 9).Value = Now
    wsCandidatesMaster.Cells(NextRow, 10).Value = Now

End Sub

