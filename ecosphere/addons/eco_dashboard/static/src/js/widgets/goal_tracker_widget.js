/** @odoo-module **/

import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class GoalTrackerWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100">
            <div class="card-header">
                <i class="fa fa-bullseye"></i>
                <span t-esc="props.config.title || 'Goal Progress'"/>
            </div>
            <div class="flex-grow-1">
                <div class="mb-3">
                    <div class="d-flex justify-content-between mb-1">
                        <span>Q3 Carbon Reduction</span>
                        <span class="text-success">75%</span>
                    </div>
                    <div class="progress" style="height: 6px; background-color: rgba(255,255,255,0.1);">
                        <div class="progress-bar bg-success" role="progressbar" style="width: 75%"></div>
                    </div>
                </div>
            </div>
        </div>
    `;
}
registry.category("eco_dashboard_widgets").add("goal", GoalTrackerWidget);
