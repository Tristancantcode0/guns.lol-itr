<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Round Button Example</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0; /* Optional background color */
        }

        .round-button {
            width: 100px;
            height: 100px;
            background-color: #7289da; /* Discord blue color */
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            line-height: 100px;
            font-size: 16px;
            text-decoration: none;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease;
        }

        .round-button:hover {
            background-color: #5a6a9f; /* Darker blue on hover */
        }
    </style>
</head>
<body>
    <a href="https://guns.lol/itr" class="round-button" target="_blank">Go</a>
</body>
</html>
