## TC49
<table>
 <tr>
  <th>
   TC49 Functional Error Codes
  </th>
  <td>
   n..5
  </td>
 </tr>
 <tr>
  <td colspan="2">
  </td>
 </tr>
</table>
<table>
 <tr>
  <th>
   Value
  </th>
  <th>
   Description
  </th>
  <th>
   Remarks
  </th>
 </tr>
 <tr>
  <td>
   0
  </td>
  <td>
   Other
  </td>
  <td>
   This value should be used only when the error does not correspond to any of the following values. It must be stressed that the value of zero should only be used for intra-release migration issues.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   12
  </td>
  <td>
   Incorrect (code) value
  </td>
  <td>
   Value of an element in a message is outside the applicable business codelist.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   15
  </td>
  <td>
   Not supported in this position
  </td>
  <td>
   The element or value is not allowed according to the applicable Rule(s) or Condition(s).
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   26
  </td>
  <td>
   Duplicate detected
  </td>
  <td>
   The same interchange is received again. Duplication is detected by reception of an interchange reference that has already been received.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   90
  </td>
  <td>
   Unknown ARC
  </td>
  <td>
   The ARC of the received message is not known, whereas it is expected to be known.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   91
  </td>
  <td>
   Duplicate LRN
  </td>
  <td>
   The LRN of the received message is already known and is therefore not unique according to the specified rules.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   92
  </td>
  <td>
   Message out of sequence
  </td>
  <td>
   The message cannot be processed, because the receiver is not in a proper state.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   93
  </td>
  <td>
   Invalid ARC
  </td>
  <td>
   The structure of the ARC does not conform to the specifications given in Rule R030.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   94
  </td>
  <td>
   Invalid Follow Up Correlation ID/ MV Correlation ID
  </td>
  <td>
   The structure of the Follow Up Correlation ID or MV Correlation ID does not conform to the specifications given in Rule R083.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   95
  </td>
  <td>
   Unknown Follow Up Correlation ID / MV Correlation ID
  </td>
  <td>
   The Follow Up Correlation ID or MV Correlation ID of the received message is not known, whereas it is expected to be known.
  </td>
  <td>
  </td>
 </tr>
</table>
