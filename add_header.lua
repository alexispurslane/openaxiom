-- Lua filter to add a header to the top of the document

function Pandoc(doc)
  -- Create a header block with some information
  local header = pandoc.Div({
    pandoc.Para({pandoc.Str("OpenAxiom System Reference Document")}),
    pandoc.Para({pandoc.Str("This document is part of the OpenAxiom TTRPG system.")}),
    pandoc.HorizontalRule(),
  }, {class = "document-header"})
  
  -- Insert the header at the beginning of the document
  table.insert(doc.blocks, 1, header)
  
  return doc
end