Attribute VB_Name = "modParserEngine"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Parser Engine
' Version 2.0.1
'==========================================================

Public Function ParseField(ByVal MailBody As String, _
                           ByVal FieldName As String) As String

    On Error GoTo ErrorHandler

    Dim ws As Object
    Dim LastRow As Long
    Dim i As Long

    Dim StartText As String
    Dim EndText As String

    Dim p1 As Long
    Dim p2 As Long

    Set ws = xlWB.Worksheets("30_ParserRules")

    LastRow = GetNextRow(ws) - 1

    For i = 2 To LastRow

        If UCase(Trim(ws.Cells(i, 2).Value)) = _
           UCase(FieldName) Then

            If UCase(Trim(ws.Cells(i, 6).Value)) <> "YES" Then
                Exit For
            End If

            StartText = ws.Cells(i, 3).Value
            EndText = ws.Cells(i, 4).Value

            p1 = InStr(1, MailBody, StartText, vbTextCompare)

            If p1 = 0 Then Exit For

            p1 = p1 + Len(StartText)

            If EndText = "\n" Then

                p2 = InStr(p1, MailBody, vbCrLf)

            Else

                p2 = InStr(p1, MailBody, EndText)

            End If

            If p2 = 0 Then

                ParseField = Trim(Mid(MailBody, p1))

            Else

                ParseField = Trim(Mid(MailBody, p1, p2 - p1))

            End If

            Exit Function

        End If

    Next i

    ParseField = ""

    Exit Function

ErrorHandler:

    LogError "modParserEngine", _
             "ParseField", _
             Err.Number, _
             Err.Description

    ParseField = ""

End Function

Public Function ParseCandidateName(ByVal Mail As Outlook.MailItem) As String

    Dim Value As String

    Value = ParseField(Mail.Body, "CandidateName")

    If Value = "" Then
        Value = ExtractCandidateName(Mail.Subject)
    End If

    ParseCandidateName = CleanText(Value)

End Function

Public Function ParseMobile(ByVal Mail As Outlook.MailItem) As String

    ParseMobile = ParseField(Mail.Body, "Mobile")

End Function

Public Function ParseEmail(ByVal Mail As Outlook.MailItem) As String

    ParseEmail = ParseField(Mail.Body, "Email")

End Function

Public Function ParseExperience(ByVal Mail As Outlook.MailItem) As String

    ParseExperience = ParseField(Mail.Body, "Experience")

End Function

Public Function ParseCurrentCTC(ByVal Mail As Outlook.MailItem) As String

    ParseCurrentCTC = ParseField(Mail.Body, "CurrentCTC")

End Function

Public Function ParseExpectedCTC(ByVal Mail As Outlook.MailItem) As String

    ParseExpectedCTC = ParseField(Mail.Body, "ExpectedCTC")

End Function

Public Function ParseNoticePeriod(ByVal Mail As Outlook.MailItem) As String

    ParseNoticePeriod = ParseField(Mail.Body, "NoticePeriod")

End Function

Public Function ParseSkills(ByVal Mail As Outlook.MailItem) As String

    ParseSkills = ParseField(Mail.Body, "Skills")

End Function

