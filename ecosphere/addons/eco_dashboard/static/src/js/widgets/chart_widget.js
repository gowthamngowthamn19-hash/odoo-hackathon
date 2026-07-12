/** @odoo-module **/

import { Component, xml, onMounted, onWillUnmount, useRef, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

export class ChartWidget extends Component {
    static template = xml`
        <div class="eco-glass-card h-100">
            <div class="card-header">
                <span t-esc="props.config.title"/>
            </div>
            <div class="flex-grow-1 position-relative" style="min-height: 200px;">
                <t t-if="state.loading">
                    <div class="eco-skeleton"></div>
                </t>
                <canvas t-ref="chartCanvas"></canvas>
            </div>
        </div>
    `;

    setup() {
        this.canvasRef = useRef("chartCanvas");
        this.chartInstance = null;
        this.state = useState({ loading: true });

        onMounted(async () => {
            await this.loadChartData();
        });

        onWillUnmount(() => {
            if (this.chartInstance) {
                this.chartInstance.destroy();
            }
        });
    }

    async loadChartData() {
        try {
            const data = await rpc("/dashboard/api/charts", { chart_type: this.props.widgetName });
            this.state.loading = false;
            this.renderChart(data);
        } catch (error) {
            console.error("Failed to load chart data", error);
            this.state.loading = false;
        }
    }

    renderChart(data) {
        if (!this.canvasRef.el || !window.Chart) return;
        
        Chart.defaults.color = '#94a3b8';
        
        this.chartInstance = new Chart(this.canvasRef.el, {
            type: this.props.config.chart_type || 'bar',
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: '#e2e8f0' }
                    }
                },
                scales: this.props.config.chart_type !== 'doughnut' ? {
                    y: { grid: { color: 'rgba(255,255,255,0.1)' } },
                    x: { grid: { color: 'rgba(255,255,255,0.1)' } }
                } : {}
            }
        });
    }
}
registry.category("eco_dashboard_widgets").add("chart", ChartWidget);
