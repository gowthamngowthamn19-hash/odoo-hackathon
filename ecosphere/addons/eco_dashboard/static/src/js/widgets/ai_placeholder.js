/** @odoo-module **/

import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class AIPlaceholderWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100" style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(30, 41, 59, 0.7)); border-color: rgba(139, 92, 246, 0.3);">
            <div class="card-header">
                <i class="fa fa-magic text-purple" style="color: #c084fc;"></i>
                <span t-esc="props.config.title || 'EcoSphere AI Insights'"/>
            </div>
            <div class="flex-grow-1">
                <p class="mb-2"><strong>Insight:</strong> Manufacturing emissions increased by 12% compared to last month.</p>
                <p class="text-muted small mb-3">Analyzing underlying power consumption data from the Assembly facility.</p>
                <button class="btn btn-sm btn-outline-light w-100" style="border-color: #c084fc; color: #c084fc;">
                    Generate Full AI Report
                </button>
            </div>
        </div>
    `;
}
registry.category("eco_dashboard_widgets").add("ai", AIPlaceholderWidget);
