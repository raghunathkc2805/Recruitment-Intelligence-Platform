Attribute VB_Name = "modAttachments"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modAttachments
'==========================================================

Public Sub SaveAttachments(ByVal Mail As Outlook.MailItem, _
                           ByVal CandidateName As String)

    On Error GoTo ErrorHandler

    Dim Atmt As Outlook.Attachment
    Dim SavePath As String
    Dim CandidateFolder As String
    Dim NextRow As Long
    Dim Ext As String

    CandidateFolder = GetSetting("CANDIDATE_FOLDER") & "\" & CleanFolderName(CandidateName)

    CreateFolder CandidateFolder
    CreateFolder CandidateFolder & "\Resumes"
    CreateFolder CandidateFolder & "\Offers"
    CreateFolder CandidateFolder & "\BGV"
    CreateFolder CandidateFolder & "\Education"
    CreateFolder CandidateFolder & "\Experience"
    CreateFolder CandidateFolder & "\Certificates"
    CreateFolder CandidateFolder & "\Photos"
    CreateFolder CandidateFolder & "\Documents"
    CreateFolder CandidateFolder & "\Others"

    For Each Atmt In Mail.Attachments

        Ext = LCase$(Mid$(Atmt.FileName, InStrRev(Atmt.FileName, ".")))

        Select Case Ext

            Case ".pdf", ".doc", ".docx"

                SavePath = CandidateFolder & "\Resumes\" & Atmt.FileName

            Case ".jpg", ".jpeg", ".png"

                SavePath = CandidateFolder & "\Photos\" & Atmt.FileName

            Case Else

                SavePath = CandidateFolder & "\Documents\" & Atmt.FileName

        End Select

        Atmt.SaveAsFile SavePath

        NextRow = GetNextRow(wsAttachments)

        wsAttachments.Cells(NextRow, 1).Value = Mail.EntryID
        wsAttachments.Cells(NextRow, 2).Value = Atmt.FileName
        wsAttachments.Cells(NextRow, 3).Value = Ext
        wsAttachments.Cells(NextRow, 4).Value = Atmt.Size
        wsAttachments.Cells(NextRow, 5).Value = SavePath
        wsAttachments.Cells(NextRow, 6).Value = CandidateName
        wsAttachments.Cells(NextRow, 7).Value = Now
        wsAttachments.Cells(NextRow, 8).Value = "Saved"

    Next

    Exit Sub

ErrorHandler:

    LogError "modAttachments", _
             "SaveAttachments", _
             Err.Number, _
             Err.Description

End Sub

Private Function CleanFolderName(ByVal FolderName As String) As String

    FolderName = Replace(FolderName, "\", "")
    FolderName = Replace(FolderName, "/", "")
    FolderName = Replace(FolderName, ":", "")
    FolderName = Replace(FolderName, "*", "")
    FolderName = Replace(FolderName, "?", "")
    FolderName = Replace(FolderName, """", "")
    FolderName = Replace(FolderName, "<", "")
    FolderName = Replace(FolderName, ">", "")
    FolderName = Replace(FolderName, "|", "")

    CleanFolderName = Trim(FolderName)

End Function

