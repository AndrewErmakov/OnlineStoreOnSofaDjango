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

function selectCategory() {
    let currentUrl = new URL(window.location.href);
    let selectedCategory = document.getElementById("selectCategory").value;

    if (selectedCategory === 'all' && currentUrl.searchParams.has('category')) {
        currentUrl.searchParams.delete('category')
    }
    if (currentUrl.searchParams.has('category')) {
        currentUrl.searchParams.set('category', selectedCategory);
    } else {
        currentUrl.searchParams.append('category', selectedCategory);
    }
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

function changePageNumber(pageNum) {
    pageNum = String(pageNum);
    let currentUrl = new URL(window.location.href);
    if (currentUrl.searchParams.has('page')) {
        currentUrl.searchParams.set('page', pageNum);
    } else {
        currentUrl.searchParams.append('page', pageNum);
    }
    window.location.href = currentUrl;
}