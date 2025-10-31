<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Java Practice IDE</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs/editor/editor.main.min.css">
    <style>
        :root {
            --primary: #1a1b26;
            --secondary: #24283b;
            --accent: #7aa2f7;
            --accent-light: #a9b1d6;
            --light: #c0caf5;
            --dark: #16161e;
            --success: #9ece6a;
            --warning: #e0af68;
            --danger: #f7768e;
            --code-bg: #1a1b26;
            --sidebar-width: 280px;
            --header-height: 60px;
            --border-radius: 12px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            --glass: rgba(30, 31, 41, 0.7);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: linear-gradient(135deg, var(--primary) 0%, var(--dark) 100%);
            color: var(--light);
            height: 100vh;
            overflow: hidden;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            background: var(--primary);
        }

        header {
            background: var(--glass);
            backdrop-filter: blur(20px);
            padding: 0 24px;
            height: var(--header-height);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            z-index: 100;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-icon {
            background: linear-gradient(135deg, var(--accent) 0%, #bb9af7 100%);
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow);
        }

        .logo h1 {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--light) 0%, var(--accent-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .controls {
            display: flex;
            gap: 12px;
        }

        .btn {
            background: rgba(122, 162, 247, 0.1);
            color: var(--accent);
            border: 1px solid rgba(122, 162, 247, 0.2);
            padding: 10px 20px;
            border-radius: var(--border-radius);
            cursor: pointer;
            font-weight: 600;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9rem;
            font-family: 'Inter', sans-serif;
            backdrop-filter: blur(10px);
        }

        .btn:hover {
            background: rgba(122, 162, 247, 0.2);
            border-color: rgba(122, 162, 247, 0.4);
            transform: translateY(-2px);
            box-shadow: var(--shadow);
        }

        .btn-run {
            background: linear-gradient(135deg, var(--success) 0%, #73daca 100%);
            color: var(--dark);
            border: none;
        }

        .btn-run:hover {
            background: linear-gradient(135deg, #8ac75a 0%, #63c6b6 100%);
            transform: translateY(-2px);
        }

        .btn-new {
            background: linear-gradient(135deg, var(--accent) 0%, #bb9af7 100%);
            color: var(--dark);
            border: none;
        }

        .btn-new:hover {
            background: linear-gradient(135deg, #6a95f5 0%, #a98af5 100%);
            transform: translateY(-2px);
        }

        .main-content {
            display: flex;
            flex: 1;
            overflow: hidden;
            padding: 20px;
            gap: 20px;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--glass);
            backdrop-filter: blur(20px);
            border-radius: var(--border-radius);
            padding: 24px;
            overflow-y: auto;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            gap: 24px;
            box-shadow: var(--shadow);
            flex-shrink: 0;
        }

        .sidebar-section {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .sidebar h2 {
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--accent-light);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }

        .file-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .file-item {
            padding: 12px 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 500;
            border: 1px solid transparent;
        }

        .file-item:hover {
            background: rgba(122, 162, 247, 0.1);
            border-color: rgba(122, 162, 247, 0.2);
        }

        .file-item.active {
            background: rgba(122, 162, 247, 0.15);
            border-color: rgba(122, 162, 247, 0.3);
            color: var(--accent);
        }

        .file-item i {
            width: 16px;
            text-align: center;
            color: var(--accent-light);
        }

        .file-item.active i {
            color: var(--accent);
        }

        .editor-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 20px;
            min-width: 0;
        }

        .editor-container {
            flex: 1;
            background: var(--code-bg);
            border-radius: var(--border-radius);
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: var(--shadow);
            display: flex;
            flex-direction: column;
        }

        .editor-header {
            background: var(--secondary);
            padding: 16px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .editor-title {
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.95rem;
        }

        .editor-actions {
            display: flex;
            gap: 8px;
        }

        .editor-actions button {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--light);
            cursor: pointer;
            padding: 8px 12px;
            border-radius: 8px;
            transition: var(--transition);
            font-size: 0.8rem;
        }

        .editor-actions button:hover {
            background: rgba(122, 162, 247, 0.1);
            border-color: rgba(122, 162, 247, 0.3);
        }

        #editor {
            flex: 1;
            width: 100%;
            border: none;
            font-family: 'JetBrains Mono', monospace !important;
        }

        .output-container {
            height: 240px;
            background: var(--glass);
            backdrop-filter: blur(20px);
            border-radius: var(--border-radius);
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            box-shadow: var(--shadow);
            flex-shrink: 0;
        }

        .output-header {
            padding: 16px 24px;
            background: rgba(36, 40, 59, 0.5);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: var(--border-radius) var(--border-radius) 0 0;
        }

        .output-title {
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.95rem;
        }

        .output-content {
            flex: 1;
            padding: 20px 24px;
            overflow-y: auto;
            font-family: 'JetBrains Mono', monospace;
            font-size: 13px;
            line-height: 1.6;
            background: rgba(26, 27, 38, 0.5);
        }

        .input-container {
            padding: 16px 24px;
            background: var(--secondary);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            display: none;
        }

        .input-container.visible {
            display: block;
        }

        .input-prompt {
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: var(--light);
            font-family: 'JetBrains Mono', monospace;
        }

        .input-field {
            width: 100%;
            padding: 12px 16px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: var(--light);
            font-family: 'JetBrains Mono', monospace;
            font-size: 14px;
            transition: var(--transition);
        }

        .input-field:focus {
            outline: none;
            border-color: var(--accent);
            background: rgba(122, 162, 247, 0.1);
        }

        .status-bar {
            background: var(--glass);
            backdrop-filter: blur(20px);
            padding: 12px 24px;
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            color: var(--accent-light);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .status-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .status-indicator {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--success);
        }

        .status-indicator.error {
            background: var(--danger);
        }

        .status-indicator.running {
            background: var(--warning);
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        .key-shortcut {
            background: rgba(255, 255, 255, 0.1);
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-family: 'JetBrains Mono', monospace;
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.3);
        }

        .output-line {
            margin-bottom: 8px;
            padding: 4px 0;
        }

        .output-error {
            color: var(--danger);
        }

        .output-success {
            color: var(--success);
        }

        .output-info {
            color: var(--accent);
        }

        .code-comment {
            color: #565f89;
            font-style: italic;
        }

        .loading {
            display: inline-block;
            width: 12px;
            height: 12px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-top: 2px solid var(--accent);
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-right: 8px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .empty-state {
            text-align: center;
            padding: 40px 20px;
            color: var(--accent-light);
        }

        .empty-state i {
            font-size: 3rem;
            margin-bottom: 16px;
            opacity: 0.5;
        }

        .empty-state p {
            font-size: 0.9rem;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">
                <div class="logo-icon">
                    <i class="fab fa-java"></i>
                </div>
                <h1>Java IDE</h1>
            </div>
            <div class="controls">
                <button class="btn btn-new" id="newClassBtn">
                    <i class="fas fa-plus"></i> New Class
                </button>
                <button class="btn" id="formatBtn">
                    <i class="fas fa-indent"></i> Format
                </button>
                <button class="btn btn-run" id="runBtn">
                    <i class="fas fa-play"></i> Run
                </button>
            </div>
        </header>

        <div class="main-content">
            <div class="sidebar">
                <div class="sidebar-section">
                    <h2>Project Files</h2>
                    <ul class="file-list" id="fileList">
                        <li class="file-item active">
                            <i class="fas fa-file-code"></i>
                            <span>Main.java</span>
                        </li>
                    </ul>
                </div>
                
                <div class="sidebar-section">
                    <h2>Common Imports</h2>
                    <ul class="file-list">
                        <li class="file-item import-item">
                            <i class="fas fa-file-import"></i>
                            <span>java.util.*</span>
                        </li>
                        <li class="file-item import-item">
                            <i class="fas fa-file-import"></i>
                            <span>java.util.Scanner</span>
                        </li>
                        <li class="file-item import-item">
                            <i class="fas fa-file-import"></i>
                            <span>java.io.*</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="editor-area">
                <div class="editor-container">
                    <div class="editor-header">
                        <div class="editor-title">
                            <i class="fas fa-file-code"></i>
                            <span id="currentFileName">Main.java</span>
                        </div>
                        <div class="editor-actions">
                            <button title="Save" id="saveBtn">
                                <i class="fas fa-save"></i> Save
                            </button>
                        </div>
                    </div>
                    <div id="editor"></div>
                </div>

                <div class="input-container" id="inputContainer">
                    <div class="input-prompt" id="inputPrompt">Enter input:</div>
                    <input type="text" class="input-field" id="inputField" placeholder="Type your input here...">
                </div>

                <div class="output-container">
                    <div class="output-header">
                        <div class="output-title">
                            <i class="fas fa-terminal"></i>
                            <span>Output</span>
                        </div>
                        <div class="editor-actions">
                            <button title="Clear Output" id="clearOutputBtn">
                                <i class="fas fa-trash"></i> Clear
                            </button>
                        </div>
                    </div>
                    <div class="output-content" id="outputContent">
                        <div class="output-line code-comment">// Program output will appear here</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="status-bar">
            <div class="status-item">
                <div class="status-indicator" id="statusIndicator"></div>
                <span id="statusText">Ready</span>
            </div>
            <div class="status-item">
                <span>Java</span>
            </div>
            <div class="status-item">
                <span class="key-shortcut">Ctrl+S</span>
                <span>Format</span>
                <span class="key-shortcut">Ctrl+Enter</span>
                <span>Run</span>
                <span class="key-shortcut">Ctrl+N</span>
                <span>New Class</span>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs/loader.min.js"></script>
    <script>
        // Store for input handling
        let inputResolver = null;
        let currentInputPrompt = "";
        let fileCounter = 1;
        let files = {
            'Main.java': `public class Main {
    public static void main(String[] args) {
        // Your code here
        System.out.println("Hello, Java!");
    }
}`
        };

        // Initialize Monaco Editor
        require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs' }});
        
        let editor;
        require(['vs/editor/editor.main'], function() {
            editor = monaco.editor.create(document.getElementById('editor'), {
                value: files['Main.java'],
                language: 'java',
                theme: 'vs-dark',
                fontSize: 14,
                fontFamily: 'JetBrains Mono, monospace',
                lineNumbers: 'on',
                roundedSelection: true,
                scrollBeyondLastLine: false,
                readOnly: false,
                cursorStyle: 'line',
                automaticLayout: true,
                minimap: { enabled: false },
                formatOnType: true,
                formatOnPaste: true,
                suggestOnTriggerCharacters: true,
                wordBasedSuggestions: true,
                snippetSuggestions: 'bottom',
                renderLineHighlight: 'all',
                scrollbar: {
                    vertical: 'visible',
                    horizontal: 'visible',
                    useShadows: false
                }
            });

            // Add keyboard shortcuts
            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, function() {
                runJavaCode();
            });

            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, function() {
                formatCode();
            });

            editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyN, function() {
                createNewClass();
            });

            // Add custom snippets for Java
            monaco.languages.registerCompletionItemProvider('java', {
                provideCompletionItems: function(model, position) {
                    const suggestions = [
                        {
                            label: 'sysout',
                            kind: monaco.languages.CompletionItemKind.Snippet,
                            insertText: 'System.out.println(${1:"${2:text}"});',
                            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                            detail: 'System.out.println()',
                            documentation: 'Prints a line to the console'
                        },
                        {
                            label: 'main',
                            kind: monaco.languages.CompletionItemKind.Snippet,
                            insertText: 'public static void main(String[] args) {\n\t${1:// code}\n}',
                            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                            detail: 'main method',
                            documentation: 'Main method entry point'
                        },
                        {
                            label: 'fori',
                            kind: monaco.languages.CompletionItemKind.Snippet,
                            insertText: 'for (int ${1:i} = 0; $1 < ${2:length}; $1++) {\n\t${3:// code}\n}',
                            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                            detail: 'for loop',
                            documentation: 'Standard for loop'
                        }
                    ];
                    return { suggestions: suggestions };
                }
            });
        });

        // DOM elements
        const runBtn = document.getElementById('runBtn');
        const formatBtn = document.getElementById('formatBtn');
        const newClassBtn = document.getElementById('newClassBtn');
        const clearOutputBtn = document.getElementById('clearOutputBtn');
        const saveBtn = document.getElementById('saveBtn');
        const outputContent = document.getElementById('outputContent');
        const fileList = document.getElementById('fileList');
        const currentFileName = document.getElementById('currentFileName');
        const statusIndicator = document.getElementById('statusIndicator');
        const statusText = document.getElementById('statusText');
        const inputContainer = document.getElementById('inputContainer');
        const inputPrompt = document.getElementById('inputPrompt');
        const inputField = document.getElementById('inputField');

        // Format code function (preserves output)
        function formatCode() {
            if (editor) {
                const currentOutput = outputContent.innerHTML;
                editor.getAction('editor.action.formatDocument').run();
                // Add a small delay to ensure formatting is complete
                setTimeout(() => {
                    outputContent.innerHTML = '<div class="output-line output-success">✓ Code formatted successfully</div>' + currentOutput;
                }, 100);
            }
        }

        // Create new class
        function createNewClass() {
            fileCounter++;
            const className = `Class${fileCounter}.java`;
            const classContent = `public class Class${fileCounter} {
    // Your class implementation here
}`;
            
            files[className] = classContent;
            
            // Add to file list
            const fileItem = document.createElement('li');
            fileItem.className = 'file-item';
            fileItem.innerHTML = `
                <i class="fas fa-file-code"></i>
                <span>${className}</span>
            `;
            fileItem.addEventListener('click', () => switchFile(className));
            fileList.appendChild(fileItem);
            
            // Switch to new file
            switchFile(className);
            
            outputContent.innerHTML = `<div class="output-line output-success">✓ Created new class: ${className}</div>` + outputContent.innerHTML;
        }

        // Switch between files
        function switchFile(fileName) {
            // Update active file in sidebar
            document.querySelectorAll('.file-item').forEach(item => item.classList.remove('active'));
            document.querySelectorAll('.file-item').forEach(item => {
                if (item.textContent.includes(fileName)) {
                    item.classList.add('active');
                }
            });
            
            // Save current file content
            if (editor) {
                files[currentFileName.textContent] = editor.getValue();
            }
            
            // Load new file content
            currentFileName.textContent = fileName;
            if (editor) {
                editor.setValue(files[fileName] || '');
            }
        }

        // Scanner input simulation
        function waitForInput(promptText) {
            return new Promise((resolve) => {
                inputResolver = resolve;
                currentInputPrompt = promptText;
                inputPrompt.textContent = promptText || "Enter input:";
                inputContainer.classList.add('visible');
                inputField.value = '';
                inputField.focus();
            });
        }

        // Handle input submission
        inputField.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && inputResolver) {
                const value = inputField.value;
                inputResolver(value);
                inputResolver = null;
                inputContainer.classList.remove('visible');
                outputContent.innerHTML += `<div class="output-line output-info">→ ${value}</div>`;
            }
        });

        // Enhanced Java execution with Scanner support
        async function runJavaCode() {
            const code = editor.getValue();
            
            // Update status
            statusIndicator.className = 'status-indicator running';
            statusText.textContent = 'Running...';
            
            try {
                // Enhanced Java execution simulation with Scanner support
                await executeJavaWithScanner(code);
                
                outputContent.innerHTML += '<div class="output-line output-success">✓ Execution completed successfully</div>';
            } catch (error) {
                outputContent.innerHTML += `<div class="output-line output-error">Error: ${error.message}</div>`;
                outputContent.innerHTML += '<div class="output-line output-error">✗ Execution failed</div>';
            } finally {
                // Update status
                statusIndicator.className = 'status-indicator';
                statusText.textContent = 'Ready';
            }
        }

        // Enhanced Java execution with Scanner simulation
        async function executeJavaWithScanner(code) {
            // Mock Scanner implementation
            const mockScanner = {
                nextLine: async function() {
                    return await waitForInput("Enter text: ");
                },
                nextInt: async function() {
                    const input = await waitForInput("Enter integer: ");
                    return parseInt(input);
                },
                nextDouble: async function() {
                    const input = await waitForInput("Enter decimal number: ");
                    return parseFloat(input);
                },
                next: async function() {
                    const input = await waitForInput("Enter word: ");
                    return input.split(' ')[0];
                },
                close: function() {
                    // Do nothing
                }
            };

            // Create execution context
            const context = {
                System: {
                    out: {
                        print: (text) => {
                            outputContent.innerHTML += `<div class="output-line">${text}</div>`;
                        },
                        println: (text) => {
                            outputContent.innerHTML += `<div class="output-line">${text}</div>`;
                        },
                        printf: (format, ...args) => {
                            let output = format;
                            args.forEach((arg, i) => {
                                output = output.replace(`%${i + 1}`, arg);
                            });
                            outputContent.innerHTML += `<div class="output-line">${output}</div>`;
                        }
                    }
                },
                Scanner: function() { return mockScanner; },
                Math: Math,
                Arrays: {
                    toString: (arr) => JSON.stringify(arr).replace(/"/g, ''),
                    sort: (arr) => arr.sort((a, b) => a - b)
                },
                Integer: {
                    parseInt: (str) => parseInt(str)
                },
                Double: {
                    parseDouble: (str) => parseFloat(str)
                }
            };

            // Extract and execute main method
            const mainMatch = code.match(/public static void main\s*\(\s*String\s*\[\]\s*args\s*\)\s*\{([\s\S]*?)\}/);
            if (!mainMatch) {
                throw new Error('No main method found');
            }

            let mainContent = mainMatch[1];
            
            // Handle imports
            if (code.includes('import java.util.Scanner;')) {
                context.Scanner = function() { return mockScanner; };
            }

            // Execute println statements and handle Scanner
            const lines = mainContent.split('\n');
            
            for (let i = 0; i < lines.length; i++) {
                let line = lines[i].trim();
                
                // Skip empty lines and comments
                if (!line || line.startsWith('//')) continue;
                
                // Handle System.out.println
                if (line.includes('System.out.println')) {
                    const contentMatch = line.match(/System\.out\.println\((.*)\);/);
                    if (contentMatch) {
                        let content = contentMatch[1];
                        // Evaluate expressions
                        if (content.includes('+')) {
                            const parts = content.split('+').map(part => {
                                let trimmed = part.trim().replace(/"/g, '');
                                // Handle variable evaluation
                                if (!trimmed.startsWith('"') && !trimmed.endsWith('"')) {
                                    return eval(trimmed);
                                }
                                return trimmed;
                            });
                            context.System.out.println(parts.join(''));
                        } else {
                            context.System.out.println(content.replace(/"/g, ''));
                        }
                    }
                }
                // Handle System.out.print
                else if (line.includes('System.out.print')) {
                    const contentMatch = line.match(/System\.out\.print\((.*)\);/);
                    if (contentMatch) {
                        let content = contentMatch[1];
                        context.System.out.print(content.replace(/"/g, ''));
                    }
                }
                // Handle variable declarations with Scanner
                else if (line.includes('Scanner') && line.includes('new Scanner')) {
                    // Scanner initialization - already handled by context
                    continue;
                }
                // Handle scanner.nextLine()
                else if (line.includes('.nextLine()')) {
                    const varMatch = line.match(/(\w+)\s*=\s*(\w+)\.nextLine\(\)/);
                    if (varMatch) {
                        const value = await mockScanner.nextLine();
                        context[varMatch[1]] = value;
                    }
                }
                // Handle scanner.nextInt()
                else if (line.includes('.nextInt()')) {
                    const varMatch = line.match(/(\w+)\s*=\s*(\w+)\.nextInt\(\)/);
                    if (varMatch) {
                        const value = await mockScanner.nextInt();
                        context[varMatch[1]] = value;
                    }
                }
                // Handle other scanner methods
                else if (line.includes('.next') && line.includes('()')) {
                    const varMatch = line.match(/(\w+)\s*=\s*(\w+)\.(\w+)\(\)/);
                    if (varMatch) {
                        const method = varMatch[3];
                        if (mockScanner[method]) {
                            const value = await mockScanner[method]();
                            context[varMatch[1]] = value;
                        }
                    }
                }
            }
        }

        // Clear output function
        function clearOutput() {
            outputContent.innerHTML = '<div class="output-line code-comment">// Output cleared</div>';
        }

        // Save current file
        function saveFile() {
            if (editor) {
                files[currentFileName.textContent] = editor.getValue();
                outputContent.innerHTML = `<div class="output-line output-success">✓ Saved ${currentFileName.textContent}</div>` + outputContent.innerHTML;
            }
        }

        // Event listeners
        runBtn.addEventListener('click', runJavaCode);
        formatBtn.addEventListener('click', formatCode);
        newClassBtn.addEventListener('click', createNewClass);
        clearOutputBtn.addEventListener('click', clearOutput);
        saveBtn.addEventListener('click', saveFile);

        // File switching
        document.querySelectorAll('.file-item').forEach(item => {
            if (!item.classList.contains('import-item')) {
                item.addEventListener('click', function() {
                    const fileName = this.querySelector('span').textContent;
                    switchFile(fileName);
                });
            }
        });

        // Import handling
        document.querySelectorAll('.import-item').forEach(item => {
            item.addEventListener('click', function() {
                const importText = this.querySelector('span').textContent;
                if (editor) {
                    const currentCode = editor.getValue();
                    if (!currentCode.includes(importText)) {
                        let newCode = currentCode;
                        if (importText === 'java.util.*' || importText === 'java.util.Scanner') {
                            if (!newCode.includes('import java.util')) {
                                newCode = `import ${importText};\n\n${newCode}`;
                            }
                        } else {
                            newCode = `import ${importText};\n\n${newCode}`;
                        }
                        editor.setValue(newCode);
                        outputContent.innerHTML = `<div class="output-line output-success">✓ Added import: ${importText}</div>` + outputContent.innerHTML;
                    }
                }
            });
        });

        // Initialize file switching for the default file
        document.querySelector('.file-item').addEventListener('click', function() {
            switchFile('Main.java');
        });
    </script>
</body>
</html>
