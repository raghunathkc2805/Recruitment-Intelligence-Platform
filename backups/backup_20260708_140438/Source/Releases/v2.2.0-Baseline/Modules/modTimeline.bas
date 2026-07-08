Attribute VB_Name = "modTimeline"
Option Explicit

Public Sub AddTimeline(ByVal CandidateID As String, _
                       ByVal CandidateName As String, _
                       ByVal Activity As String, _
                       ByVal ReferenceID As String)

    Dim NextRow As Long

    NextRow = GetNextRow( _
        xlWB.Worksheets("24_CandidateTimeline"))

    With xlWB.Worksheets("24_CandidateTimeline")

        .Cells(NextRow, 1).Value = _
            "TL" & Format(Now, "yyyymmddhhnnss")

        .Cells(NextRow, 2).Value = CandidateID
        .Cells(NextRow, 3).Value = CandidateName
        .Cells(NextRow, 4).Value = Activity
        .Cells(NextRow, 5).Value = Now
        .Cells(NextRow, 6).Value = CurrentUser
        .Cells(NextRow, 8).Value = ReferenceID

    End With

End Sub

