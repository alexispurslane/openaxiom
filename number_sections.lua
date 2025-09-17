heading_count = {0, 0, 0, 0, 0, 0}

function get_chapter_number()
    -- Get the input filename
    local input_file = PANDOC_STATE.input_files[1]
    if not input_file then return nil end
  
    -- Extract just the filename (not the full path)
    local filename = input_file:match("([^/\\]+)$")
  
    -- Read toc_order.json
    local file = io.open("toc_order.json", "r")
    if not file then return nil end
  
    local content = file:read("*all")
    file:close()
  
    -- Parse the JSON array manually to find the position of our file
    -- This is a simple approach that works for the specific format in toc_order.json
    local files = {}
    for file_match in content:gmatch('"([^"]+)"') do
        if file_match ~= "files" then
            table.insert(files, file_match)
        end
    end
  
    -- Find our file in the list
    for i, file_name in ipairs(files) do
        if file_name == filename then
            return i
        end
    end
  
    return nil
end

chapter_number = get_chapter_number()

function Pandoc(doc)
    if chapter_number then
        local header = pandoc.Header(1, chapter_number .. ". " .. pandoc.utils.stringify(doc.meta.title))
        table.insert(doc.blocks, 1, header)
    end
    return doc
end


function Header(el)
    el.level = el.level + 1
    heading_count[1] = chapter_number

    if el.level >= 2 then
        for i = el.level + 1, 6 do
            heading_count[i] = 0
        end
        heading_count[el.level] = heading_count[el.level] + 1
        
        number_string = ""
        for i = 1, 6 do
            if heading_count[i] and heading_count[i] ~= 0 then
                number_string = number_string .. heading_count[i] .. "."
            end
        end
            
        table.insert(el.content, 1, pandoc.Str(number_string .. " "))
    end
    return el
end

-- Remove all the list indentation code since it was adding spaces after bullet points
-- which is not what we want
