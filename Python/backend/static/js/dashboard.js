import { getDashboard } from "./api.js";
import { initFilters, getCurrentFilters } from "./filters.js";

// Stubs — Tasks 12/13 replace these with real rendering.
function renderKpis(kpis) {
    console.log("renderKpis", kpis);
}

function renderCharts(charts) {
    console.log("renderCharts", charts);
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
