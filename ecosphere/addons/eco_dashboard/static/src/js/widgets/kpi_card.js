/** @odoo-module **/

import { Component, xml, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { dashboardStore } from "../dashboard_store";

export class KPICard extends Component {
    static template = xml`
        <div class="eco-glass-card h-100">
            <div class="card-header">
                <i t-att-class="'fa ' + props.config.icon"></i>
                <span t-esc="props.config.title"/>
            </div>
            <div class="eco-kpi-value">
                <span t-esc="kpiData.value !== undefined ? kpiData.value : '0'"/>
                <span style="font-size: 1rem;" t-esc="kpiData.suffix || ''"/>
            </div>
        </div>
    `;

    setup() {
        this.store = useState(dashboardStore);
    }

    get kpiData() {
        return this.store.kpis[this.props.widgetName] || {};
    }
}
registry.category("eco_dashboard_widgets").add("kpi", KPICard);
