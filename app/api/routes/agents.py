from flask import Blueprint, Response, stream_with_context

agents_bp = Blueprint('agents', __name__)

def generate_events():
    """Generator function to create dummy SSE events"""
    # Sample dummy events
    events = [
        {'id': 1, 'message': 'Hello from agent!'},
        {'id': 2, 'message': 'How can I help you today?'},
        {'id': 3, 'message': 'Processing your request...'},
        {'id': 4, 'message': 'Task completed!'}
    ]
    
    for event in events:
        data = f"data: {str(event)}\n\n"
        yield data
        # You can add a small delay here if needed
        import time
        time.sleep(1)

@agents_bp.route('/chat', methods=['GET'])
def get_agents():
    """SSE endpoint that streams dummy events"""
    return Response(
        stream_with_context(generate_events()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive'
        }
    ) 