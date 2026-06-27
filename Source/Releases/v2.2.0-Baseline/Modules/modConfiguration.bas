Attribute VB_Name = "modConfiguration"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modConfiguration
'==========================================================

Public Function InitializeApplication() As Boolean

    On Error GoTo ErrorHandler

    InitializeApplication = False

    Set xlApp = CreateObject("Excel.Application")

    xlApp.Visible = False
    xlApp.DisplayAlerts = False

    Set xlWB = xlApp.Workbooks.Open(GetSetting("DATABASE_FILE"))

    Set wsSettings = xlWB.Worksheets(SH_SETTINGS)
    Set wsProcessed = xlWB.Worksheets(SH_PROCESSED)
    Set wsResources = xlWB.Worksheets(SH_RESOURCES)
    Set wsCandidates = xlWB.Worksheets(SH_CANDIDATES)
    Set wsOffers = xlWB.Worksheets(SH_OFFERS)
    Set wsInterviews = xlWB.Worksheets(SH_INTERVIEWS)
    Set wsBGV = xlWB.Worksheets(SH_BGV)
    Set wsDeviation = xlWB.Worksheets(SH_DEVIATION)
    Set wsResume = xlWB.Worksheets(SH_RESUME)
    Set wsNATS = xlWB.Worksheets(SH_NATS)
    Set wsNAPS = xlWB.Worksheets(SH_NAPS)
    Set wsRecruiters = xlWB.Worksheets(SH_RECRUITERS)
    Set wsCustomers = xlWB.Worksheets(SH_CUSTOMERS)
    Set wsKPI = xlWB.Worksheets(SH_KPI)
    Set wsError = xlWB.Worksheets(SH_ERROR)
    Set wsAudit = xlWB.Worksheets(SH_AUDIT)
    Set wsDashboard = xlWB.Worksheets(SH_DASHBOARD)
    Set wsLookup = xlWB.Worksheets(SH_LOOKUP)
    Set wsAdvanced = xlWB.Worksheets(SH_ADVANCED)
    Set wsMailIndex = xlWB.Worksheets(SH_MAILINDEX)
    Set wsMailTypes = xlWB.Worksheets(SH_MAILTYPES)
    Set wsFolderMaster = xlWB.Worksheets(SH_FOLDERMASTER)
    Set wsAttachments = xlWB.Worksheets(SH_ATTACHMENTS)
    Set wsCandidatesMaster = xlWB.Worksheets(SH_CANDIDATES_MASTER)

    CurrentUser = Environ$("USERNAME")
    CurrentVersion = APP_VERSION

    EmailsScanned = 0
    EmailsProcessed = 0
    EmailsSkipped = 0
    EmailsFailed = 0

    StartTime = Now

    AppInitialized = True
    InitializeApplication = True

    Exit Function

ErrorHandler:

    AppInitialized = False
    InitializeApplication = False

End Function

Public Sub CloseApplication()

    On Error Resume Next

    EndTime = Now

    If Not xlWB Is Nothing Then
        xlWB.Save
        xlWB.Close False
    End If

    If Not xlApp Is Nothing Then
        xlApp.Quit
    End If

    Set wsSettings = Nothing
    Set wsProcessed = Nothing
    Set wsResources = Nothing
    Set wsCandidates = Nothing
    Set wsOffers = Nothing
    Set wsInterviews = Nothing
    Set wsBGV = Nothing
    Set wsDeviation = Nothing
    Set wsResume = Nothing
    Set wsNATS = Nothing
    Set wsNAPS = Nothing
    Set wsRecruiters = Nothing
    Set wsCustomers = Nothing
    Set wsKPI = Nothing
    Set wsError = Nothing
    Set wsAudit = Nothing
    Set wsDashboard = Nothing
    Set wsLookup = Nothing
    Set wsAdvanced = Nothing
    Set wsMailIndex = Nothing
    Set wsMailTypes = Nothing
    Set wsFolderMaster = Nothing
    Set wsAttachments = Nothing
    Set wsCandidatesMaster = Nothing

    Set xlWB = Nothing
    Set xlApp = Nothing

    AppInitialized = False

End Sub
