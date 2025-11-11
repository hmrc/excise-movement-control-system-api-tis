## TC63
<table>
 <tr>
  <th>
   TC63 Reason to refuse update of economic operators
  </th>
  <td>
   n..3
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
   8
  </td>
  <td>
   Trader Authorisation already exists (creation)
  </td>
  <td>
   A record with the specified Trader Excise Number already exists.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   9
  </td>
  <td>
   Tax warehouse already exists (creation)
  </td>
  <td>
   A record with the specified Reference of Tax Warehouse already exists.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   10
  </td>
  <td>
   Temporary authorisation already exists (creation)
  </td>
  <td>
   A record with the specified Temporary Authorisation Reference already exists.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   11
  </td>
  <td>
   Trader Authorisation not found (Update / Deletion)
  </td>
  <td>
   The Update / Deletion operation cannot be performed since the specified Trader Excise Number cannot be found.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   12
  </td>
  <td>
   Tax warehouse not found (Update / Deletion)
  </td>
  <td>
   The Update / Deletion operation cannot be performed since the specified Reference of Tax Warehouse cannot be found.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   13
  </td>
  <td>
   Temporary authorisation not found (Update / Deletion)
  </td>
  <td>
   The Update / Deletion operation cannot be performed since the specified Temporary Authorisation Reference cannot be found.
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
   27
  </td>
  <td>
   Inconsistency between Excise number and Excise office
  </td>
  <td>
   The specified Excise office cannot be used for the specified Excise number (applies to all authorisations).
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   41
  </td>
  <td>
   Only a warehouse keeper may be allowed to use a tax warehouse
  </td>
  <td>
   The Data Group (USING) TAX WAREHOUSE only applies to tax warehouse keepers.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   42
  </td>
  <td>
   Invalid Reference of Tax Warehouse (R204 violation)
  </td>
  <td>
   The specified Tax Warehouse Reference is not a valid &lt;TAX WAREHOUSE.Reference of Tax Warehouse&gt; or it is invalid according to Rule R204.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   43
  </td>
  <td>
   Missing Authorised Warehouse Keeper referencing Tax Warehouse (R205 violation)
  </td>
  <td>
   The specified Tax Warehouse Reference is not a valid &lt;(USING) TAX WAREHOUSE.Reference of Tax Warehouse&gt; defined in Rule R205.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   44
  </td>
  <td>
   &lt;Trader Excise Number&gt; is missing (Cond157 violation)
  </td>
  <td>
   The Consignor Trader Excise Number is not specified for the Temporary Authorisation that is not flagged as Small Wine Producer.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   45
  </td>
  <td>
   Invalid value for &lt;Excise Product Code&gt; (Rule212 violation)
  </td>
  <td>
   The specified Excise Product Codes are other than ‘W200’ and ‘W300’ for the Temporary Authorisation that is flagged as Small Wine Producer.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   46
  </td>
  <td>
   The National Administration of the Temporary Authorisation and the declared Consignor is the same (R233 violation)
  </td>
  <td>
   The National Administration of the Consignor is the same with the National Administration the Temporary Authorisation is registered for
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   112
  </td>
  <td>
   Incorrect (code) value
  </td>
  <td>
   Value of an element in a message is outside the applicable business Codelist.
  </td>
  <td>
  </td>
 </tr>
 <tr>
  <td>
   115
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
</table>
