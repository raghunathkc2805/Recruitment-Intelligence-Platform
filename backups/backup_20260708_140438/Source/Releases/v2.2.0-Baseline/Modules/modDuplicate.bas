Attribute VB_Name = "modDuplicate"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modDuplicate
'==========================================================

Public Function IsMailProcessed(ByVal EntryID As String) As Boolean

    On Error GoTo ErrorHandler

    Dim LastRow As Long
    Dim i As Long

    LastRow = GetNextRow(wsProcessed) - 1

    If LastRow < 2 Then
        IsMailProcessed = False
        Exit Function
    End If

    For i = 2 To LastRow

        If Trim(CStr(wsProcessed.Cells(i, 1).Value)) = Trim(EntryID) Then

            IsMailProcessed = True
            Exit Function

        End If

    Next i

    IsMailProcessed = False

    Exit Function

ErrorHandler:

    LogError "modDuplicate", "IsMailProcessed", Err.Number, Err.Description

    IsMailProcessed = False

End Function

Public Sub AddProcessedMail(ByVal EntryID As String, _
                            ByVal Subject As String, _
                            ByVal Sender As String, _
                            ByVal ReceivedTime As Date)

    On Error GoTo ErrorHandler

    Dim NextRow As Long

    NextRow = GetNextRow(wsProcessed)

    wsProcessed.Cells(NextRow, 1).Value = EntryID
    wsProcessed.Cells(NextRow, 2).Value = Subject
    wsProcessed.Cells(NextRow, 3).Value = Sender
    wsProcessed.Cells(NextRow, 4).Value = ReceivedTime
    wsProcessed.Cells(NextRow, 5).Value = Now

    Exit Sub

ErrorHandler:

    LogError "modDuplicate", "AddProcessedMail", Err.Number, Err.Description

End Sub

