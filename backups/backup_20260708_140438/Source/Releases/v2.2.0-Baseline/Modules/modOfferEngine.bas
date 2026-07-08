Attribute VB_Name = "modOfferEngine"
Option Explicit

'==========================================================
' Recruitment Automation Suite
' Module : modOfferEngine
'==========================================================

Public Sub ProcessOfferMail(ByVal Mail As Outlook.MailItem)

    On Error GoTo ErrorHandler

    Dim CandidateName As String
    Dim CandidateID As String
    Dim OfferID As String
    Dim NextRow As Long

    CandidateName = ExtractCandidateName(Mail.Subject)

    If CandidateName = "" Then Exit Sub

    CreateCandidate CandidateName

    CandidateID = GetCandidateID(CandidateName)

    OfferID = GenerateNextOfferID()

    NextRow = GetNextRow(wsOffers)

    wsOffers.Cells(NextRow, 1).Value = OfferID
    wsOffers.Cells(NextRow, 2).Value = CandidateID
    wsOffers.Cells(NextRow, 3).Value = CandidateName
    wsOffers.Cells(NextRow, 10).Value = Date
    wsOffers.Cells(NextRow, 14).Value = "Released"
    wsOffers.Cells(NextRow, 17).Value = Mail.Subject
    wsOffers.Cells(NextRow, 18).Value = Mail.SenderName
    wsOffers.Cells(NextRow, 19).Value = Mail.SenderEmailAddress
    wsOffers.Cells(NextRow, 20).Value = Mail.EntryID
    wsOffers.Cells(NextRow, 22).Value = Now
    wsOffers.Cells(NextRow, 23).Value = Now

    AddTimeline CandidateID, _
                CandidateName, _
                "Offer Released", _
                OfferID

    Exit Sub

ErrorHandler:

    LogError "modOfferEngine", _
             "ProcessOfferMail", _
             Err.Number, _
             Err.Description

End Sub

