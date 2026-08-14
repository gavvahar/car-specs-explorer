import { getDashboard } from "./api.js";
import { initFilters, getCurrentFilters } from "./filters.js";
import { renderCharts } from "./charts.js";
import { renderKpis } from "./kpis.js";
import { renderLeaderboard } from "./leaderboard.js";

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
