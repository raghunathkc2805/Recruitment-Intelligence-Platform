Attribute VB_Name = "modLogger"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modLogger
'==========================================================

Public Sub LogError(ByVal ModuleName As String, _
                    ByVal ProcedureName As String, _
                    ByVal ErrorNumber As Long, _
                    ByVal ErrorDescription As String)

    On Error Resume Next

    Dim NextRow As Long

    NextRow = wsError.Cells(wsError.Rows.Count, 1).End(-4162).Row + 1

    wsError.Cells(NextRow, 1).Value = Now
    wsError.Cells(NextRow, 2).Value = ModuleName
    wsError.Cells(NextRow, 3).Value = ProcedureName
    wsError.Cells(NextRow, 4).Value = ErrorNumber
    wsError.Cells(NextRow, 5).Value = ErrorDescription
    wsError.Cells(NextRow, 6).Value = CurrentUser

End Sub

Public Sub WriteAudit(ByVal Activity As String)

    On Error Resume Next

    Dim NextRow As Long

    NextRow = wsAudit.Cells(wsAudit.Rows.Count, 1).End(-4162).Row + 1

    wsAudit.Cells(NextRow, 1).Value = Now
    wsAudit.Cells(NextRow, 2).Value = CurrentUser
    wsAudit.Cells(NextRow, 3).Value = Activity
    wsAudit.Cells(NextRow, 4).Value = APP_VERSION

End Sub

