Attribute VB_Name = "modGlobals"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Global Variables
'==========================================================

'Excel Objects
Public xlApp As Object
Public xlWB As Object

'Worksheets
Public wsSettings As Object
Public wsProcessed As Object
Public wsResources As Object
Public wsCandidates As Object
Public wsOffers As Object
Public wsInterviews As Object
Public wsBGV As Object
Public wsDeviation As Object
Public wsResume As Object
Public wsNATS As Object
Public wsNAPS As Object
Public wsRecruiters As Object
Public wsCustomers As Object
Public wsKPI As Object
Public wsError As Object
Public wsAudit As Object
Public wsDashboard As Object
Public wsLookup As Object
Public wsAdvanced As Object
Public wsMailIndex As Object
Public wsMailTypes As Object
Public wsFolderMaster As Object
Public wsAttachments As Object
Public wsCandidatesMaster As Object

'Application
Public AppInitialized As Boolean
Public CurrentUser As String
Public CurrentVersion As String

'Statistics
Public EmailsScanned As Long
Public EmailsProcessed As Long
Public EmailsSkipped As Long
Public EmailsFailed As Long

'Execution
Public StartTime As Date
Public EndTime As Date
