// Store a unique identifier for this tab
const tabId = Date.now().toString();
sessionStorage.setItem('openaxiomTabId', tabId);

// Broadcast to other tabs that this tab is now active
const channel = new BroadcastChannel('openaxiom_channel');
channel.postMessage({type: 'newTab', id: tabId});

// Listen for messages from other tabs
channel.addEventListener('message', function(event) {
    if (event.data.type === 'newTab' && event.data.id !== tabId) {
        // Close this tab if another one opens
        window.close();
    }
});

// Set up socket connection for live reload
const socket = io();
socket.on('reload', function(data) {
    location.reload();
});