function selectSorting() {
    let currentUrl = new URL(window.location.href);
    let sortingType = document.getElementById("selectSorting").value;

    if (sortingType === 'default' && currentUrl.searchParams.has('sort_by')) {
        currentUrl.searchParams.delete('sort_by')
    } else if (currentUrl.searchParams.has('sort_by')) {
        currentUrl.searchParams.set('sort_by', sortingType);
    } else {
        currentUrl.searchParams.append('sort_by', sortingType);
    }

    window.location.href = currentUrl;
}

function selectRubric() {
    let currentUrl = new URL(window.location.href);
    let selectedRubric = document.getElementById("selectRubric").value;

    if (selectedRubric === 'all' && currentUrl.searchParams.has('rubric')) {
        currentUrl.searchParams.delete('rubric')
    }
    if (currentUrl.searchParams.has('rubric')) {
        currentUrl.searchParams.set('rubric', selectedRubric);
    } else {
        currentUrl.searchParams.append('rubric', selectedRubric);
    }
    let option = document.getElementById('rubric_' + selectedRubric);
    option.setAttribute('selected', true);

    window.location.href = currentUrl;
}

function searchProduct() {
    let currentUrl = new URL(window.location.href);
    let searchSymbols = document.getElementById("searchSymbols").value;
    if (searchSymbols.trim() !== '') {
        if (currentUrl.searchParams.has('search')) {
            currentUrl.searchParams.set('search', searchSymbols);
        } else {
            currentUrl.searchParams.append('search', searchSymbols);
        }
        window.location.href = currentUrl;
    }
}
