// Function to color the core oracle table cells based on their content
function colorOracleTable() {
    // Find all core oracle tables
    const oracleTables = document.querySelectorAll('table.core-oracle-table');
    
    // Define color mappings for different result types
    const colorMap = {
        'Yes, and…': '#81c784',  // Darker green
        'Yes, but…': '#dce775',  // Light green
        'Yes': '#aed581',        // Medium green
        'No, but…': '#ffb74d',   // Orange
        'No, and…': '#e57373',   // Darker red
        'No': '#ef9a9a'          // Medium red
    };
    
    // Process each oracle table
    oracleTables.forEach(table => {
        // Get all cells in the table
        const cells = table.querySelectorAll('td');
        
        // Process each cell
        cells.forEach(cell => {
            const text = cell.textContent.trim();
            
            // Apply color based on cell content
            if (colorMap[text]) {
                cell.style.backgroundColor = colorMap[text];
                cell.style.fontWeight = 'bold';
            }
        });
    });
}

// Run the coloring function when the page loads
document.addEventListener('DOMContentLoaded', colorOracleTable);