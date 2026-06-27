Attribute VB_Name = "modMain"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Main Controller
'==========================================================

Public Sub RunRecruitmentAutomation()

    On Error GoTo ErrorHandler

    If InitializeApplication = False Then
        MsgBox "Failed to initialize application.", vbCritical
        Exit Sub
    End If

    WriteAudit "Recruitment Automation Started"

    ScanOutlook

    WriteAudit "Recruitment Automation Completed"

    SaveWorkbook

    MsgBox _
        "Recruitment Automation Completed" & vbCrLf & vbCrLf & _
        "Emails Scanned   : " & EmailsScanned & vbCrLf & _
        "Emails Processed : " & EmailsProcessed & vbCrLf & _
        "Emails Skipped   : " & EmailsSkipped & vbCrLf & _
        "Errors           : " & EmailsFailed, _
        vbInformation, APP_NAME

    CloseApplication

    Exit Sub

ErrorHandler:

    LogError "modMain", _
             "RunRecruitmentAutomation", _
             Err.Number, _
             Err.Description

    MsgBox Err.Description, vbCritical

    CloseApplication

End Sub

