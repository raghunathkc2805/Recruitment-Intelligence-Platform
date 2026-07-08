Attribute VB_Name = "modSettingsEngine"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Settings Engine
' Version 2.1.0
'==========================================================

Public Function GetSetting(ByVal SettingName As String) As String

    On Error GoTo ErrorHandler

    Dim LastRow As Long
    Dim i As Long

    LastRow = GetNextRow(wsSettings) - 1

    For i = 2 To LastRow

        If UCase(Trim(wsSettings.Cells(i, 1).Value)) = _
           UCase(Trim(SettingName)) Then

            GetSetting = Trim(CStr(wsSettings.Cells(i, 2).Value))
            Exit Function

        End If

    Next i

    GetSetting = ""

    Exit Function

ErrorHandler:

    LogError "modSettingsEngine", _
             "GetSetting", _
             Err.Number, _
             Err.Description

    GetSetting = ""

End Function

Public Function GetSettingBoolean(ByVal SettingName As String) As Boolean

    GetSettingBoolean = _
        (UCase(GetSetting(SettingName)) = "YES")

End Function

Public Function GetSettingNumber(ByVal SettingName As String) As Long

    If IsNumeric(GetSetting(SettingName)) Then
        GetSettingNumber = CLng(GetSetting(SettingName))
    Else
        GetSettingNumber = 0
    End If

End Function

