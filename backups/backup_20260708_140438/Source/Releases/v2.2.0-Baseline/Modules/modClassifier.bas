Attribute VB_Name = "modClassifier"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modClassifier
'==========================================================

Public Function GetMailType(ByVal Subject As String) As String

    On Error GoTo ErrorHandler

    Dim LastRow As Long
    Dim i As Long
    Dim Keyword As String

    Subject = UCase(Trim(Subject))

    LastRow = GetNextRow(wsMailTypes) - 1

    If LastRow < 2 Then
        GetMailType = "UNKNOWN"
        Exit Function
    End If

    For i = 2 To LastRow

        Keyword = UCase(Trim(CStr(wsMailTypes.Cells(i, 1).Value)))

        If Keyword <> "" Then

            If InStr(1, Subject, Keyword, vbTextCompare) > 0 Then

                GetMailType = Trim(CStr(wsMailTypes.Cells(i, 2).Value))
                Exit Function

            End If

        End If

    Next i

    GetMailType = "UNKNOWN"

    Exit Function

ErrorHandler:

    LogError "modClassifier", _
             "GetMailType", _
             Err.Number, _
             Err.Description

    GetMailType = "UNKNOWN"

End Function

Public Function IsResourceMail(ByVal Subject As String) As Boolean

    IsResourceMail = (GetMailType(Subject) = "RESOURCE")

End Function

Public Function IsOfferMail(ByVal Subject As String) As Boolean

    IsOfferMail = (GetMailType(Subject) = "OFFER")

End Function

Public Function IsInterviewMail(ByVal Subject As String) As Boolean

    IsInterviewMail = (GetMailType(Subject) = "INTERVIEW")

End Function

Public Function IsBGVMail(ByVal Subject As String) As Boolean

    IsBGVMail = (GetMailType(Subject) = "BGV")

End Function

Public Function IsDeviationMail(ByVal Subject As String) As Boolean

    IsDeviationMail = (GetMailType(Subject) = "DEVIATION")

End Function

Public Function IsResumeMail(ByVal Subject As String) As Boolean

    IsResumeMail = (GetMailType(Subject) = "RESUME")

End Function

Public Function IsNATSMail(ByVal Subject As String) As Boolean

    IsNATSMail = (GetMailType(Subject) = "NATS")

End Function

Public Function IsNAPSMail(ByVal Subject As String) As Boolean

    IsNAPSMail = (GetMailType(Subject) = "NAPS")

End Function

