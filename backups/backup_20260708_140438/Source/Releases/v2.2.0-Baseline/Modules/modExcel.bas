Attribute VB_Name = "modExcel"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modExcel
'==========================================================

Public Function OpenDatabase() As Boolean

    On Error GoTo ErrorHandler

    If xlApp Is Nothing Then
        Set xlApp = CreateObject("Excel.Application")
    End If

    xlApp.Visible = False
    xlApp.DisplayAlerts = False

    If xlWB Is Nothing Then
        Set xlWB = xlApp.Workbooks.Open(GetSetting("DATABASE_FILE"))
    End If

    OpenDatabase = True

    Exit Function

ErrorHandler:

    LogError "modExcel", "OpenDatabase", Err.Number, Err.Description

    OpenDatabase = False

End Function

Public Function SaveWorkbook() As Boolean

    On Error GoTo ErrorHandler

    xlWB.Save

    SaveWorkbook = True

    Exit Function

ErrorHandler:

    LogError "modExcel", "SaveWorkbook", Err.Number, Err.Description

    SaveWorkbook = False

End Function

Public Function CloseDatabase() As Boolean

    On Error GoTo ErrorHandler

    If Not xlWB Is Nothing Then
        xlWB.Close SaveChanges:=True
    End If

    If Not xlApp Is Nothing Then
        xlApp.Quit
    End If

    Set xlWB = Nothing
    Set xlApp = Nothing

    CloseDatabase = True

    Exit Function

ErrorHandler:

    LogError "modExcel", "CloseDatabase", Err.Number, Err.Description

    CloseDatabase = False

End Function

Public Function GetWorksheet(ByVal SheetName As String) As Object

    On Error Resume Next

    Set GetWorksheet = xlWB.Worksheets(SheetName)

End Function
