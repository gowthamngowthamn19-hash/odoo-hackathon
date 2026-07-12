/** @odoo-module **/

import { Component, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class RecentActivityWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100">
            <div class="card-header">
                <i class="fa fa-history"></i>
                <span t-esc="props.config.title || 'Recent Activity'"/>
            </div>
            <div class="flex-grow-1 overflow-auto">
                <ul class="list-unstyled">
                    <li class="mb-2 pb-2 border-bottom border-secondary">
                        <small class="text-muted d-block">10 mins ago</small>
                        <span>Marketing Dept completed CSR Goal</span>
                    </li>
                    <li class="mb-2 pb-2 border-bottom border-secondary">
                        <small class="text-muted d-block">1 hr ago</small>
                        <span>New ESG Policy Published</span>
                    </li>
                </ul>
            </div>
        </div>
    `;
}
registry.category("eco_dashboard_widgets").add("activity", RecentActivityWidget);
