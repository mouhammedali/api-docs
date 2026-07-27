-- Converts single-column Word "tables" (used as makeshift code blocks / preformatted
-- boxes) into real fenced code blocks, reading literal text straight from the AST
-- so none of pandoc's markdown-escaping ever applies to this content.

local function inlines_to_text(inlines)
  local lines = {}
  local cur = {}
  for _, inline in ipairs(inlines) do
    local t = inline.t
    if t == "LineBreak" or t == "SoftBreak" then
      table.insert(lines, table.concat(cur))
      cur = {}
    elseif t == "Str" then
      table.insert(cur, inline.text)
    elseif t == "Space" then
      table.insert(cur, " ")
    elseif t == "Span" or t == "Emph" or t == "Strong" or t == "Underline"
        or t == "SmallCaps" or t == "Strikeout" then
      table.insert(cur, inlines_to_text(inline.content))
    elseif t == "Quoted" then
      table.insert(cur, inlines_to_text(inline.content))
    elseif t == "Code" then
      table.insert(cur, inline.text)
    end
  end
  table.insert(lines, table.concat(cur))
  return table.concat(lines, "\n")
end

local function blocks_to_text(blocks)
  local lines = {}
  for _, block in ipairs(blocks) do
    if block.t == "Para" or block.t == "Plain" then
      table.insert(lines, inlines_to_text(block.content))
    elseif block.t == "CodeBlock" then
      table.insert(lines, block.text)
    end
  end
  return table.concat(lines, "\n")
end

function Table(el)
  if #el.colspecs ~= 1 then
    return nil
  end

  local textLines = {}

  if el.head and el.head.rows then
    for _, row in ipairs(el.head.rows) do
      for _, cell in ipairs(row.cells) do
        table.insert(textLines, blocks_to_text(cell.contents))
      end
    end
  end

  for _, body in ipairs(el.bodies) do
    if body.head then
      for _, row in ipairs(body.head) do
        for _, cell in ipairs(row.cells) do
          table.insert(textLines, blocks_to_text(cell.contents))
        end
      end
    end
    for _, row in ipairs(body.body) do
      for _, cell in ipairs(row.cells) do
        table.insert(textLines, blocks_to_text(cell.contents))
      end
    end
  end

  local text = table.concat(textLines, "\n")
  text = text:gsub("^%s+", ""):gsub("%s+$", "")
  if text == "" then
    return nil
  end

  local lang = ""
  if text:match("^[%[{]") then
    lang = "json"
  end

  return pandoc.CodeBlock(text, pandoc.Attr("", {lang}))
end
