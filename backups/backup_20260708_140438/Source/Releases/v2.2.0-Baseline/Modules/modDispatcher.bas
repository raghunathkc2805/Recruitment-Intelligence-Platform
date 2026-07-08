Attribute VB_Name = "modDispatcher"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Dispatcher Engine
' Version 2.0.1
'==========================================================

Public Sub DispatchMail(ByVal Mail As Outlook.MailItem, _
                        ByVal FolderPath As String)

    On Error GoTo ErrorHandler

    Dim MailType As String

    MailType = GetMailType(Mail.Subject)

    Select Case UCase(MailType)

        Case "RESOURCE"

            ProcessResourceMail Mail, FolderPath

        Case "OFFER"

            ProcessOfferMail Mail

        Case "INTERVIEW"

            ProcessInterviewMail Mail

        Case "BGV"

            ProcessBGVMail Mail

        Case "DEVIATION"

            ProcessDeviationMail Mail

        Case "NATS"

            ProcessNATSMail Mail

        Case "NAPS"

            ProcessNAPSMail Mail

        Case Else

            EmailsSkipped = EmailsSkipped + 1

    End Select

    Exit Sub

ErrorHandler:

    LogError "modDispatcher", _
             "DispatchMail", _
             Err.Number, _
             Err.Description

End Sub

