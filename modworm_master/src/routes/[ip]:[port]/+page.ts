import { error} from '@sveltejs/kit';
import { BASE_URL } from '$lib/env';

export const ssr = false;

export async function load({ fetch, params }) {
	const port = params.port;
	const ip = params.ip;

	async function try_discover() {
		const response = await fetch(`${BASE_URL}/nmap/${ip}/${port}`);
		console.log(response.status);
		if (!response.ok) error(response.status, await response.json());
		const servers = await response.json();

		for (const server of servers) {
			if (server.address === ip && server.port === port) return true;
		}
		return false;
	}

	return { discovered:await try_discover(), ip, port};
}



