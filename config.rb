destination_dir = "excise-movement-control-system-api-tis-4-2"

pages_to_redirect = [
  "business-codelists.html",
  "business-rules.html",
  "conditions.html",
  "data-item-formats.html",
  "index.html",
  "messagetypes.html",
  "process_flows.html",
  "rules.html",
  "technical-codelists.html",
  "validation-rules.html"
]

pages_to_redirect.each { |page| redirect page, to: "../#{destination_dir}/#{page}" }
