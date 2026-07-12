/** @odoo-module **/

import { reactive } from "@odoo/owl";

export const dashboardStore = reactive({
    layout: [],
    kpis: {},
    availableWidgets: {},
    filters: {
        department_id: null,
        date_range: 'this_month'
    },
    setInitialData(data) {
        this.layout = data.layout || [];
        this.kpis = data.kpis || {};
        this.availableWidgets = data.available_widgets || {};
    }
});
