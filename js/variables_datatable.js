function loadTable(id, file){
    // Fetch the CSV file
    fetch(file).then(response => response.text()).then(data => {
        // Parse CSV data
        const rows = data.split("\n").slice(0, -1);
        const headerRow = rows[0].split(",");
        const tableData = rows.slice(1).map(row => row.split(","));

        // Create labels
        let labels = {
            placeholder: "Search...",
            searchTitle: "Search within table",
            perPage: "entries per page",
            noRows: "No entries found",
            info: "Showing {start} to {end} of {rows} entries",
            noResults: "No results match your search query"
        };
        if (file.match(/_fr/g)) {
            labels = {
                placeholder: "Rechercher...",
                searchTitle: "Rechercher dans le tableau",
                perPage: "entrées par page",
                noRows: "Aucune entrée trouvée",
                info: "Affichage de {start} à {end} sur {rows} entrées",
                noResults: "Aucun résultat ne correspond à votre requête de recherche"
            };
        }

        // Get table id
        const table = "#" + id
        // Initialize the DataTable
        new simpleDatatables.DataTable(table, {
            data: {
                headings: headerRow,
                data: tableData
            },
            fixedColumns: false,
            labels: labels
        });
    });
}
