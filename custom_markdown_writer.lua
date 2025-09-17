-- Custom Pandoc writer for Markdown with increased list indentation
-- and proper table rendering

local layout = pandoc.layout
local concat, blankline, hang, space = 
  layout.concat, layout.blankline, layout.hang, layout.space

-- Use scaffolding to reduce boilerplate
Writer = pandoc.scaffolding.Writer

-- Inline elements
Writer.Inline.Str = function(el)
  return el.text
end

Writer.Inline.Space = function()
  return " "
end

Writer.Inline.SoftBreak = function()
  return " "
end

Writer.Inline.LineBreak = function()
  return "\n"
end

Writer.Inline.Emph = function(el)
  return concat{"*", Writer.Inlines(el.content), "*"}
end

Writer.Inline.Strong = function(el)
  -- Handle potential nested strong elements from org parsing
  -- Check if content is a single Strong element to avoid double wrapping
  if #el.content == 1 and el.content[1].tag == "Strong" then
    return Writer.Inlines(el.content)
  else
    return concat{"**", Writer.Inlines(el.content), "**"}
  end
end

Writer.Inline.Code = function(el)
  return concat{"`", el.text, "`"}
end

Writer.Inline.Quoted = function(el)
  -- Default to double quotes
  return concat{"\"", Writer.Inlines(el.content), "\""}
end

Writer.Inline.RawInline = function(el)
  if el.format == "html" then
    return el.text
  else
    return ""
  end
end

Writer.Inline.Link = function(el)
  local text = Writer.Inlines(el.content)
  return concat{"[", text, "](", el.target, ")"}
end

Writer.Inline.Image = function(el)
  local text = Writer.Inlines(el.caption)
  return concat{"![", text, "](", el.src, ")"}
end

Writer.Inline.Span = function(el)
  return Writer.Inlines(el.content)
end

-- Block elements
Writer.Block.Header = function(el)
  local tag = string.rep("#", el.level)
  return concat{tag, " ", Writer.Inlines(el.content), blankline}
end

Writer.Block.Para = function(el)
  return concat{Writer.Inlines(el.content), blankline}
end

Writer.Block.Plain = function(el)
  return Writer.Inlines(el.content)
end

Writer.Block.BlockQuote = function(el)
  -- Process each block individually to preserve formatting and structure
  local result = {}
  for i, block in ipairs(el.content) do
    local block_content = Writer.Block(block)
    -- Convert the layout Doc to string properly
    local block_string = pandoc.layout.render(block_content)
    -- Add > prefix to each line
    for line in string.gmatch(block_string, "[^\r\n]*") do
      if line ~= "" then
        result[#result + 1] = "> " .. line
      else
        result[#result + 1] = ">"
      end
    end
  end
  return concat{concat(result, "\n"), "\n"}
end

Writer.Block.CodeBlock = function(el)
  return concat{"```", el.classes[1] or "", "\n", el.text, "\n```\n\n"}
end

Writer.Block.RawBlock = function(el)
  if el.format == "html" then
    return el.text .. "\n"
  else
    return ""
  end
end

Writer.Block.Table = function(el)
  local result = {}
  
  -- Render the table header
  if el.head and #el.head.rows > 0 then
    local header_row = "|"
    local separator_row = "|"
    
    -- Process the first row of the header
    local first_header_row = el.head.rows[1]
    for i, cell in ipairs(first_header_row.cells) do
      -- Use Writer.Blocks to preserve formatting
      local cell_content = Writer.Blocks(cell.contents)
      header_row = header_row .. " " .. cell_content .. " |"
      -- Create simple separator
      separator_row = separator_row .. "--------|"
    end
    
    result[#result + 1] = header_row
    result[#result + 1] = separator_row
  end
  
  -- Render the table bodies
  for _, body in ipairs(el.bodies) do
    for _, row in ipairs(body.body) do
      local row_str = "|"
      for i, cell in ipairs(row.cells) do
        -- Use Writer.Blocks to preserve formatting
        local cell_content = Writer.Blocks(cell.contents)
        row_str = row_str .. " " .. cell_content .. " |"
      end
      result[#result + 1] = row_str
    end
  end
  
  return concat{concat(result, "\n"), "\n\n"}
end

Writer.Block.Div = function(el)
  -- Just render the content of the div
  return Writer.Blocks(el.content)
end

-- Custom bullet list with increased indentation (3 spaces more than default)
Writer.Block.BulletList = function(el)
  local result = {}
  for i=1,#el.content do
    -- Default markdown uses 2 spaces for indentation, we'll use 5 (2 + 3)
    result[#result + 1] = hang(Writer.Blocks(el.content[i], blankline), 5, concat{"-",space})
  end
  return concat(result, blankline)
end

-- Custom ordered list with increased indentation (3 spaces more than default)
Writer.Block.OrderedList = function(el)
  local result = {}
  local num = el.start
  for i=1,#el.content do
    local numstr = string.format("%d.", num)
    -- Default markdown uses varying spaces based on number width, we'll add 3 more
    local width = string.len(numstr) + 4  -- 1 space + 3 extra
    result[#result + 1] = hang(Writer.Blocks(el.content[i], blankline), width, concat{numstr," "})
    num = num + 1
  end
  return concat(result, blankline)
end