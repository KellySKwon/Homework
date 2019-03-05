'### Easy

'* Create a script that will loop through each year of stock data and grab the total amount of volume each stock had over the year.
'* You will also need to display the ticker symbol to coincide with the total volume.
'* Your result should look as follows (note: all solution images are for 2015 data).

Sub ticker()

Dim ws As Worksheet
Dim rowCount As Long
Dim j As Long

Dim tickerName As String
Dim totalVolume As Long

For Each ws In Worksheets
    j = 2
    rowCount = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    For i = 2 To rowCount
    
        If ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1).Value Then
        ws.Cells(j, 9).Value = ws.Cells(i, 1).Value
        ws.Cells(j, 10).Value = Application.WorksheetFunction.SumIf(ws.Range("A:A"), ws.Cells(j, 9).Value, ws.Range("G:G"))
        j = j + 1
        End If
    
    Next i
    
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Total Stock Volume"

Next

End Sub

