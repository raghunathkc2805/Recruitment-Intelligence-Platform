Attribute VB_Name = "modUtilities"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modUtilities
'==========================================================

Public Function GetNextRow(ByVal ws As Object) As Long

    If ws.Cells(1, 1).Value = "" Then
        GetNextRow = 1
    Else
        GetNextRow = ws.Cells(ws.Rows.Count, 1).End(-4162).Row + 1
    End If

End Function

Public Function FileExists(ByVal FileName As String) As Boolean

    FileExists = (Dir(FileName) <> "")

End Function

Public Function FolderExists(ByVal FolderName As String) As Boolean

    FolderExists = (Dir(FolderName, vbDirectory) <> "")

End Function

Public Sub CreateFolder(ByVal FolderName As String)

    If FolderName = "" Then Exit Sub

    If Not FolderExists(FolderName) Then
        MkDir FolderName
    End If

End Sub

Public Function CleanText(ByVal txt As String) As String

    txt = Replace(txt, vbCr, "")
    txt = Replace(txt, vbLf, "")
    txt = Replace(txt, vbTab, "")
    txt = Trim(txt)

    Do While InStr(txt, "  ") > 0
        txt = Replace(txt, "  ", " ")
    Loop

    CleanText = txt

End Function

Public Function SafeText(ByVal Value As Variant) As String

    If IsNull(Value) Then
        SafeText = ""
    Else
        SafeText = Trim(CStr(Value))
    End If

End Function

Public Function SheetExists(ByVal SheetName As String) As Boolean

    Dim ws As Object

    On Error Resume Next

    Set ws = xlWB.Worksheets(SheetName)

    SheetExists = Not ws Is Nothing

    Set ws = Nothing

End Function

Public Function CleanFolderName(ByVal FolderName As String) As String

    FolderName = Trim(FolderName)

    FolderName = Replace(FolderName, "\", "")
    FolderName = Replace(FolderName, "/", "")
    FolderName = Replace(FolderName, ":", "")
    FolderName = Replace(FolderName, "*", "")
    FolderName = Replace(FolderName, "?", "")
    FolderName = Replace(FolderName, """", "")
    FolderName = Replace(FolderName, "<", "")
    FolderName = Replace(FolderName, ">", "")
    FolderName = Replace(FolderName, "|", "")

    Do While InStr(FolderName, "  ") > 0
        FolderName = Replace(FolderName, "  ", " ")
    Loop

    CleanFolderName = FolderName

End Function

Public Function GetFileExtension(ByVal FileName As String) As String

    If InStrRev(FileName, ".") = 0 Then
        GetFileExtension = ""
    Else
        GetFileExtension = LCase(Mid(FileName, InStrRev(FileName, ".")))
    End If

End Function

Public Function IsResumeFile(ByVal FileName As String) As Boolean

    Select Case GetFileExtension(FileName)

        Case ".pdf", ".doc", ".docx"

            IsResumeFile = True

        Case Else

            IsResumeFile = False

    End Select

End Function

Public Function IsImageFile(ByVal FileName As String) As Boolean

    Select Case GetFileExtension(FileName)

        Case ".jpg", ".jpeg", ".png", ".bmp"

            IsImageFile = True

        Case Else

            IsImageFile = False

    End Select

End Function

Public Function GenerateCandidateID() As String

    GenerateCandidateID = _
        "CAN" & Format(Now, "yyyymmddhhnnss")

End Function
'==========================================================
' Candidate ID Generator
'==========================================================

Public Function GenerateNextCandidateID() As String

    On Error GoTo ErrorHandler

    Dim NextNo As Long

    NextNo = CLng(xlWB.Worksheets("24_CandidateSequence").Range("A2").Value)

    GenerateNextCandidateID = "CAN" & Format(NextNo, "000000")

    xlWB.Worksheets("24_CandidateSequence").Range("A2").Value = NextNo + 1

    Exit Function

ErrorHandler:

    LogError "modUtilities", _
             "GenerateNextCandidateID", _
             Err.Number, _
             Err.Description

    GenerateNextCandidateID = ""

End Function
Public Function GenerateNextOfferID() As String

    Static OfferNo As Long

    OfferNo = OfferNo + 1

    GenerateNextOfferID = _
        "OFF" & Format(OfferNo, "000000")

End Function
'==========================================================
' Extract Candidate Name from Subject
'==========================================================

Public Function ExtractCandidateName(ByVal Subject As String) As String

    Dim Parts() As String

    Subject = Trim(Subject)

    Parts = Split(Subject, "-")

    If UBound(Parts) >= 0 Then
        ExtractCandidateName = CleanText(Parts(0))
    Else
        ExtractCandidateName = ""
    End If

End Function

