Attribute VB_Name = "modFolders"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modFolders
'==========================================================

Public Function GetFolderList() As Collection

    On Error GoTo ErrorHandler

    Dim FolderList As New Collection
    Dim LastRow As Long
    Dim i As Long

    LastRow = GetNextRow(wsFolderMaster) - 1

    If LastRow < 2 Then
        Set GetFolderList = FolderList
        Exit Function
    End If

    For i = 2 To LastRow

        If UCase(Trim(CStr(wsFolderMaster.Cells(i, 2).Value))) = "YES" Then

            FolderList.Add Trim(CStr(wsFolderMaster.Cells(i, 1).Value))

        End If

    Next i

    Set GetFolderList = FolderList

    Exit Function

ErrorHandler:

    LogError "modFolders", "GetFolderList", Err.Number, Err.Description

    Set GetFolderList = New Collection

End Function

Public Function FolderEnabled(ByVal FolderName As String) As Boolean

    On Error GoTo ErrorHandler

    Dim LastRow As Long
    Dim i As Long

    LastRow = GetNextRow(wsFolderMaster) - 1

    If LastRow < 2 Then
        FolderEnabled = False
        Exit Function
    End If

    For i = 2 To LastRow

        If UCase(Trim(CStr(wsFolderMaster.Cells(i, 1).Value))) = UCase(FolderName) Then

            FolderEnabled = (UCase(Trim(CStr(wsFolderMaster.Cells(i, 2).Value))) = "YES")

            Exit Function

        End If

    Next i

    FolderEnabled = False

    Exit Function

ErrorHandler:

    LogError "modFolders", "FolderEnabled", Err.Number, Err.Description

    FolderEnabled = False

End Function
