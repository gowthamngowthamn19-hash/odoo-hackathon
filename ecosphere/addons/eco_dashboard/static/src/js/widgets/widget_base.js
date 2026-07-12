/** @odoo-module **/

import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { dashboardStore } from "../dashboard_store";

export class PlaceholderWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100 d-flex align-items-center justify-content-center">
            <span class="text-muted">Widget Type Not Found: <t t-esc="props.config.title || props.widgetName"/></span>
        </div>
    `;
}
registry.category("eco_dashboard_widgets").add("placeholder", PlaceholderWidget);
