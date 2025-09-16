// Function to color the NPC reactions table cells based on their content
function colorNPCReactionsTable() {
    // Get the actual table element (the ID is on a parent div)
    const table = document.querySelector('.npc-reactions-table');
    
    // If no table is found, exit early
    if (!table) {
        return;
    }
    
    // Define CSS class mappings for different reaction types
    const colorMap = {
        'Hostile': '#ef9a9a',
        'Unfriendly': '#ffcccb',
        'Cold': '#ffab91',
        'Cool': '#ffe082',
        'Neutral': '#fff59d',
        'Helpful': '#a5d6a7',
        'Enthusiastic': '#81c784'
    };
    
    // Get all cells in the table
    const cells = table.querySelectorAll('td');
    
    // Process each cell
    cells.forEach(cell => {
        const text = cell.textContent.trim();
        
        // Apply CSS class based on cell content
        if (colorMap[text]) {
            cell.style.backgroundColor = colorMap[text]
        }
    });
}

// Run the coloring function when the page loads
document.addEventListener('DOMContentLoaded', colorNPCReactionsTable);
