import express from 'express';
import cors from 'cors';

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.post('/chat', (req, res) => {
  const { input } = req.body;

  // Set headers for streaming
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  // Generate dummy responses
  const responses = [
    "Processing your input...",
    `Received: ${input}`,
    "Generating response...",
    "Almost done...",
    "Here's your final response!",
  ];

  let counter = 0;

  // Stream responses with delays
  const interval = setInterval(() => {
    if (counter < responses.length) {
      res.write(`data: ${JSON.stringify({ message: responses[counter] })}\n\n`);
      counter++;
    } else {
      clearInterval(interval);
      res.end();
    }
  }, 1000);

  // Handle client disconnect
  req.on('close', () => {
    clearInterval(interval);
    res.end();
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
