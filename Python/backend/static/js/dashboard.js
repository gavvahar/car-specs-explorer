import { getDashboard } from "./api.js";
import { initFilters, getCurrentFilters } from "./filters.js";
import { renderCharts } from "./charts.js";

// Stub — Task 13 replaces this with real rendering.
function renderKpis(kpis) {
    console.log("renderKpis", kpis);
}

function renderLeaderboard(leaderboard) {
    console.log("renderLeaderboard", leaderboard);
}

async function refresh() {
    const filters = getCurrentFilters();
    try {
        const data = await getDashboard(filters);
        renderKpis(data.kpis);
        renderCharts(data.charts);
        renderLeaderboard(data.leaderboard);
    } catch (error) {
        console.error("Failed to load dashboard data:", error);
    }
}

async function init() {
    await initFilters(refresh);
    await refresh();
}

init();
