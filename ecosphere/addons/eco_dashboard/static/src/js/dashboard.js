/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";
import { dashboardStore } from "./dashboard_store";
import { loadJS } from "@web/core/assets";

export class EcoDashboard extends Component {
    setup() {
        this.store = useState(dashboardStore);
        this.state = useState({
            isLoaded: false
        });

        onWillStart(async () => {
            if (!window.Chart) {
                await loadJS("https://cdn.jsdelivr.net/npm/chart.js");
            }
            const data = await rpc("/dashboard/api/init", {});
            this.store.setInitialData(data);
            this.state.isLoaded = true;
        });
    }

    getWidgetComponent(widgetName) {
        const widgetConfig = this.store.availableWidgets[widgetName];
        if (!widgetConfig) return null;
        
        const widgetRegistry = registry.category("eco_dashboard_widgets");
        if (widgetRegistry.contains(widgetConfig.type)) {
            return widgetRegistry.get(widgetConfig.type);
        }
        return widgetRegistry.get("placeholder");
    }
    
    getWidgetConfig(widgetName) {
        return this.store.availableWidgets[widgetName] || {};
    }
}

EcoDashboard.template = "eco_dashboard.Main";
registry.category("actions").add("eco_dashboard.main", EcoDashboard);
