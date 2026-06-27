Attribute VB_Name = "modMailScanner"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modMailScanner
'==========================================================

Public Sub ScanOutlook()

    On Error GoTo ErrorHandler

    Dim NS As Outlook.NameSpace
    Dim Inbox As Outlook.Folder
    Dim FolderList As Collection
    Dim FolderName As Variant

    Set NS = Application.GetNamespace("MAPI")
    Set FolderList = GetFolderList()

    For Each FolderName In FolderList

        Select Case UCase(CStr(FolderName))

            Case "INBOX"

                Set Inbox = NS.GetDefaultFolder(olFolderInbox)
                ScanFolder Inbox

            Case "SENT ITEMS"

                Set Inbox = NS.GetDefaultFolder(olFolderSentMail)
                ScanFolder Inbox

            Case "DELETED ITEMS"

                Set Inbox = NS.GetDefaultFolder(olFolderDeletedItems)
                ScanFolder Inbox

        End Select

    Next FolderName

    Exit Sub

ErrorHandler:

    LogError "modMailScanner", _
             "ScanOutlook", _
             Err.Number, _
             Err.Description

End Sub

Private Sub ScanFolder(ByVal oFolder As Outlook.Folder)

    On Error GoTo ErrorHandler

    Dim itm As Object
    Dim SubFolder As Outlook.Folder

    For Each itm In oFolder.Items

        If TypeName(itm) = "MailItem" Then

            EmailsScanned = EmailsScanned + 1

            ProcessMail itm, oFolder.FolderPath

        End If

    Next itm

    For Each SubFolder In oFolder.Folders

        ScanFolder SubFolder

    Next SubFolder

    Exit Sub

ErrorHandler:

    LogError "modMailScanner", _
             "ScanFolder", _
             Err.Number, _
             Err.Description

End Sub

Private Sub ProcessMail(ByVal Mail As Outlook.MailItem, _
                        ByVal FolderPath As String)

    On Error GoTo ErrorHandler

    Dim MailType As String

    If IsMailProcessed(Mail.EntryID) Then

        EmailsSkipped = EmailsSkipped + 1
        Exit Sub

    End If

   DispatchMail Mail, FolderPath

    AddProcessedMail _
        Mail.EntryID, _
        Mail.Subject, _
        Mail.SenderName, _
        Mail.ReceivedTime

    EmailsProcessed = EmailsProcessed + 1

    Exit Sub

ErrorHandler:

    EmailsFailed = EmailsFailed + 1

    LogError "modMailScanner", _
             "ProcessMail", _
             Err.Number, _
             Err.Description

End Sub

