
def map(km):
    km.add(":", "console.command ''", ["global"], "Command prompt")
    km.add("?", "console.view.help", ["global"], "View help")
    km.add("C", "console.view.commands", ["global"], "View commands")
    km.add("O", "console.view.options", ["global"], "View options")
    km.add("E", "console.view.eventlog", ["global"], "View event log")
    km.add("Q", "console.exit", ["global"], "Exit immediately")
    km.add("q", "console.view.pop", ["global"], "Exit the current view")
    km.add("-", "console.layout.cycle", ["global"], "Cycle to next layout")
    km.add("shift tab", "console.panes.next", ["global"], "Focus next layout pane")
    km.add("P", "console.view.flow @focus", ["global"], "View flow details")

    km.add("g", "console.nav.start", ["global"], "Go to start")
    km.add("G", "console.nav.end", ["global"], "Go to end")
    km.add("k", "console.nav.up", ["global"], "Up")
    km.add("j", "console.nav.down", ["global"], "Down")
    km.add("l", "console.nav.right", ["global"], "Right")
    km.add("h", "console.nav.left", ["global"], "Left")
    km.add("tab", "console.nav.next", ["global"], "Next")
    km.add("enter", "console.nav.select", ["global"], "Select")
    km.add(" ", "console.nav.pagedown", ["global"], "Page down")
    km.add("ctrl f", "console.nav.pagedown", ["global"], "Page down")
    km.add("ctrl b", "console.nav.pageup", ["global"], "Page up")

    km.add("i", "console.command set intercept=", ["global"], "Set intercept")
    km.add("W", "console.command set save_stream_file=", ["global"], "Stream to file")
    km.add("A", "flow.resume @all", ["flowlist", "flowview"], "Resume all intercepted flows")
    km.add("a", "flow.resume @focus", ["flowlist", "flowview"], "Resume this intercepted flow")
    km.add(
        "b", "console.command cut.save s.content|@focus ''",
        ["flowlist", "flowview"],
        "Save response body to file"
    )
    km.add("d", "view.remove @focus", ["flowlist", "flowview"], "Delete flow from view")
    km.add("D", "view.duplicate @focus", ["flowlist", "flowview"], "Duplicate flow")
    km.add(
        "e",
        "console.choose.cmd Format export.formats "
        "console.command export.file {choice} @focus ''",
        ["flowlist", "flowview"],
        "Export this flow to file"
    )
    km.add("f", "console.command set view_filter=", ["flowlist"], "Set view filter")
    km.add("F", "set console_focus_follow=toggle", ["flowlist"], "Set focus follow")
    km.add(
        "ctrl l",
        "console.command cut.clip ",
        ["flowlist", "flowview"],
        "Send cuts to clipboard"
    )
    km.add("L", "console.command view.load ", ["flowlist"], "Load flows from file")
    km.add("m", "flow.mark.toggle @focus", ["flowlist"], "Toggle mark on this flow")
    km.add("M", "view.marked.toggle", ["flowlist"], "Toggle viewing marked flows")
    km.add(
        "n",
        "console.command view.create get https://google.com",
        ["flowlist"],
        "Create a new flow"
    )
    km.add(
        "o",
        "console.choose.cmd Order view.order.options "
        "set console_order={choice}",
        ["flowlist"],
        "Set flow list order"
    )
    km.add("r", "replay.client @focus", ["flowlist", "flowview"], "Replay this flow")
    km.add("S", "console.command replay.server ", ["flowlist"], "Start server replay")
    km.add("v", "set console_order_reversed=toggle", ["flowlist"], "Reverse flow list order")
    km.add("U", "flow.mark @all false", ["flowlist"], "Un-set all marks")
    km.add("w", "console.command save.file @shown ", ["flowlist"], "Save listed flows to file")
    km.add("V", "flow.revert @focus", ["flowlist", "flowview"], "Revert changes to this flow")
    km.add("X", "flow.kill @focus", ["flowlist"], "Kill this flow")
    km.add("z", "view.remove @all", ["flowlist"], "Clear flow list")
    km.add("Z", "view.remove @hidden", ["flowlist"], "Purge all flows not showing")
    km.add(
        "|",
        "console.command script.run @focus ",
        ["flowlist", "flowview"],
        "Run a script on this flow"
    )

    km.add(
        "e",
        "console.choose.cmd Part console.edit.focus.options "
        "console.edit.focus {choice}",
        ["flowview"],
        "Edit a flow component"
    )
    km.add(
        "f",
        "view.setval.toggle @focus fullcontents",
        ["flowview"],
        "Toggle viewing full contents on this flow",
    )
    km.add("w", "console.command save.file @focus ", ["flowview"], "Save flow to file")
    km.add(" ", "view.focus.next", ["flowview"], "Go to next flow")

    km.add(
        "v",
        "console.choose \"View Part\" request,response "
        "console.bodyview @focus {choice}",
        ["flowview"],
        "View flow body in an external viewer"
    )
    km.add("p", "view.focus.prev", ["flowview"], "Go to previous flow")
    km.add("m", "console.flowview.mode.set", ["flowview"], "Set flow view mode")
    km.add(
        "z",
        "console.choose \"Part\" request,response "
        "flow.encode.toggle @focus {choice}",
        ["flowview"],
        "Encode/decode flow body"
    )

    km.add("L", "console.command options.load ", ["options"], "Load from file")
    km.add("S", "console.command options.save ", ["options"], "Save to file")
    km.add("D", "options.reset", ["options"], "Reset all options")
    km.add("d", "console.options.reset.current", ["options"], "Reset this option")

    km.add("a", "console.grideditor.add", ["grideditor"], "Add a row after cursor")
    km.add("A", "console.grideditor.insert", ["grideditor"], "Insert a row before cursor")
    km.add("d", "console.grideditor.delete", ["grideditor"], "Delete this row")
    km.add(
        "r",
        "console.command console.grideditor.readfile",
        ["grideditor"],
        "Read unescaped data from file"
    )
    km.add(
        "R",
        "console.command console.grideditor.readfile_escaped",
        ["grideditor"],
        "Read a Python-style escaped string from file"
    )
    km.add("e", "console.grideditor.editor", ["grideditor"], "Edit in external editor")
