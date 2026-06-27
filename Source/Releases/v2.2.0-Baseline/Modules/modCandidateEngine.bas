Attribute VB_Name = "modCandidateEngine"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modCandidateEngine
'==========================================================

Public Function GetCandidateID(ByVal CandidateName As String) As String

    On Error GoTo ErrorHandler

    Dim LastRow As Long
    Dim i As Long

    LastRow = GetNextRow(wsCandidatesMaster) - 1

    If LastRow >= 2 Then

        For i = 2 To LastRow

            If UCase(Trim(wsCandidatesMaster.Cells(i, 2).Value)) = _
               UCase(Trim(CandidateName)) Then

                GetCandidateID = _
                    wsCandidatesMaster.Cells(i, 1).Value

                Exit Function

            End If

        Next i

    End If

    GetCandidateID = GenerateNextCandidateID()

    Exit Function

ErrorHandler:

    LogError "modCandidateEngine", _
             "GetCandidateID", _
             Err.Number, _
             Err.Description

    GetCandidateID = ""

End Function

Public Function CandidateExists(ByVal CandidateName As String) As Boolean

    On Error GoTo ErrorHandler

    Dim LastRow As Long
    Dim i As Long

    LastRow = GetNextRow(wsCandidatesMaster) - 1

    If LastRow < 2 Then

        CandidateExists = False
        Exit Function

    End If

    For i = 2 To LastRow

        If UCase(Trim(wsCandidatesMaster.Cells(i, 2).Value)) = _
           UCase(Trim(CandidateName)) Then

            CandidateExists = True
            Exit Function

        End If

    Next i

    CandidateExists = False

    Exit Function

ErrorHandler:

    LogError "modCandidateEngine", _
             "CandidateExists", _
             Err.Number, _
             Err.Description

    CandidateExists = False

End Function

Public Sub CreateCandidate(ByVal CandidateName As String)

    On Error GoTo ErrorHandler

    Dim NextRow As Long
    Dim CandidateID As String
    Dim FolderPath As String

    If CandidateExists(CandidateName) Then Exit Sub

    CandidateID = GetCandidateID(CandidateName)

    FolderPath = _
        GetSetting(GetSetting("CANDIDATE_FOLDER")) & "\" & _
        CleanFolderName(CandidateName)

    NextRow = GetNextRow(wsCandidatesMaster)

    wsCandidatesMaster.Cells(NextRow, 1).Value = CandidateID
    wsCandidatesMaster.Cells(NextRow, 2).Value = CandidateName
    wsCandidatesMaster.Cells(NextRow, 19).Value = FolderPath
    wsCandidatesMaster.Cells(NextRow, 28).Value = Now
    wsCandidatesMaster.Cells(NextRow, 29).Value = Now

    CreateFolder FolderPath
    CreateFolder FolderPath & "\Resumes"
    CreateFolder FolderPath & "\Offers"
    CreateFolder FolderPath & "\BGV"
    CreateFolder FolderPath & "\Education"
    CreateFolder FolderPath & "\Experience"
    CreateFolder FolderPath & "\Certificates"
    CreateFolder FolderPath & "\Photos"
    CreateFolder FolderPath & "\Documents"
    CreateFolder FolderPath & "\Others"

    Exit Sub

ErrorHandler:

    LogError "modCandidateEngine", _
             "CreateCandidate", _
             Err.Number, _
             Err.Description

End Sub

